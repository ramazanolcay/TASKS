#%%


import psycopg2


conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")

cur=conn.cursor()

#TABLO İÇERİKLERİ

sql1 ='''CREATE TABLE users(
   id SERIAL PRIMARY KEY,
   email VARCHAR(50),
   password VARCHAR(50)
)'''

sql2 ='''CREATE TABLE urunler(
   id SERIAL PRIMARY KEY,
   urunAdi VARCHAR(50),
   fiyat INTEGER,
   puan INTEGER
)'''

sql3 ='''CREATE TABLE mail(
   ordered_mail_id SERIAL PRIMARY KEY,
   mail_id INTEGER,
   checker BOOLEAN NOT NULL DEFAULT False
)'''  
    
sql4 ='''CREATE TABLE orders(
    OrderId SERIAL PRIMARY KEY,
    Date TIMESTAMP,
    user_id INTEGER,
    urunId INTEGER,
    fiyat INTEGER
)'''    
    
#TABLO OLUŞTURMA

cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql4)
conn.commit()
#%%
# Fake mail ve şifreler
import numpy as np
from faker import Faker
myfake = Faker()

import psycopg2


conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")
cur=conn.cursor()

for i in range(1001):
    try:
        mail = str(myfake.email())
        cur.execute("SELECT EXISTS(SELECT email FROM users WHERE email=(%s))",(mail,))
        a = cur.fetchall()
        if (a[0][0]) == False:
            password = str(myfake.password())
            cur.execute("INSERT INTO users (email,password) VALUES (%s,%s)",(mail,password,)) 
    except:
        pass
    

conn.commit()


#%%
#OLUŞTURDUĞUM ÜRÜNLER
import psycopg2


conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")
cur=conn.cursor()
productname_array = ["Su","Kola","Döner","Zurna Dürüm","Pizza", "Pide", "Lahmacun","Ayran", "Burger", "Kumpir", "Etli Ekmek","Tost", "Sandviç"]
productprice_array = [3,8,20,40,80, 50, 20,6, 40, 60, 50,40, 30]
productrate_array = [3,8,2,4,8, 5, 10,6, 4, 6, 5,9, 3]
for i in range(len(productname_array)):
    cur.execute("INSERT INTO urunler (urunAdi,fiyat,puan) VALUES (%s,%s,%s)",(productname_array[i],productprice_array[i],productrate_array[i]))

conn.commit()











