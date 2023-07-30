import psycopg2


conn = psycopg2.connect(dbname="personalportfoliodb", user="personalportfoliodb_user", password="juHwaTKoNUZabyTdsieEST23C5WiB3rH", host="dpg-cj2305b438ig33nd48b0-a.frankfurt-postgres.render.com", port="5432")
cur = conn.cursor()
conn.autocommit = True