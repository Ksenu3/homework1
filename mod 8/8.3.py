import mysql.connector
from geopy.distance import geodesic



yheys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Sopopopohopo8',
    autocommit=True
    )

kentta1 = input("Anna ekan lentoaseman ICAO-koodi: ")
kentta2 = input("Anna tokan lentoaseman ICAO-koodi: ")

sql = "select latitude_deg, longitude_deg from airport where ident = %s;"

kursori = yhteys.cursor()

kursori.execute(sql, (kentta1, ))
kordinaatit1 = kursori.fetchone()

kursori.execute(sql, (kentta2, ))
kordinaatit2 =  kursori.fetchone()

etaisyys = geodesic(kordinaatit1, kordinaatit2).kilometers

print(f"Lentokenttien välinen etäisyys on {etaisyys:2f} km")