import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Sopopopohopo8',
         autocommit=True
         )

koodi = input("Anna lentoaseman ICAO-koodi: ")

sql = "select name, municipality from airport where ident = %s;"
kursori = yhteys.cursor()
kursori.execute(sql, (koodi,))

tulos = kursori.fetchone()
print(tulos)