from . import connector
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
import re

connector.cur.execute("""CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(1000),
            email VARCHAR(1000),
            password VARCHAR(1000));"""
)

# Create your views here.

def home(response):
    return render(response, "main/HomePage.html", {})

def education(response):
    template = loader.get_template('main/EducationPage.html')
    context = {}
    return HttpResponse(template.render(context, response))

def experience(response):
    return render(response, "main/ExperiencePage.html", {})

def signup(response):
    if response.method == "POST":
        username = response.POST["username"]
        email = response.POST["email"]
        password = response.POST["password"]

        connector.cur.execute("""SELECT id FROM Users WHERE email = %s;""", [email])

        try:
            id = ((connector.cur.fetchall()[0])[0])
            ErrorMessage = "Email is already being used."
            return render(response, "main/SignUpPage.html", {"ErrorMessage": ErrorMessage})  
        
        except:
            pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            if (re.search(pattern, email)):
                connector.cur.execute("""
        INSERT INTO Users (username, email, password) VALUES
                                (%s, %s, %s);""", [username, email, password])
                connector.conn.commit()

                return redirect("/home")

            else:
                ErrorMessage = "Please type in an valid email."
                return render(response, "main/SignUpPage.html", {"ErrorMessage": ErrorMessage})            

    return render(response, "main/SignUpPage.html", {})

def login(response):
    if response.method == "POST":
        username = response.POST["username"]
        email = response.POST["email"]
        password = response.POST["password"]

        connector.cur.execute("""SELECT id FROM Users WHERE username = %s AND password = %s AND email = %s;""", [username, password, email])

        try:
            id = ((connector.cur.fetchall()[0])[0])
            return redirect("/home")

        except:
            ErrorMessage = "Wrong login details."
            return render(response, "main/LoginPage.html", {"ErrorMessage": ErrorMessage})
       
        
    return render(response, "main/LoginPage.html", {})

# retrieve data from login or signup
# if signup check fi datas valid, if so then insert data into table
# if not then send error message, then redirect user to the other pages

# for login check if data matches the data in database, if so let them through, else error message
# redirect user to page