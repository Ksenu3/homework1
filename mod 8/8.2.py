import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Sopopopohopo8',
    autocommit=True
    )

maa = input("Anna maakoodi: ")

sql = "select type, count(*) from airport where iso_country = %s group by type;"

kursori = yhteys.cursor()
kursori.execute(sql, (maa,))

tulos = kursori.fetchall()
print(tulos)


