import time 
import json 
from kafka import KafkaProducer
import datetime
import psycopg2
import random

conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")
cur=conn.cursor()


ORDER_KAFKA_TOPIC="order_details"
ORDER_LIMIT = 50

producer=KafkaProducer(bootstrap_servers="localhost:9092")



for i in range(1,ORDER_LIMIT):
    rnd = random.randint(1,1000)
    cur.execute("SELECT * FROM users WHERE (id = (%s))",(rnd,))
    my_user_query = cur.fetchall()
    rnd = random.randint(1,13)
    cur.execute("SELECT * FROM urunler WHERE (id = (%s))",(rnd,))
    my_item_query = cur.fetchall()

    date =datetime.datetime.now()

    cur.execute('INSERT INTO orders(Date,user_id,urunId,fiyat) VALUES(%s, %s, %s, %s)',(date,my_user_query[0][0],my_item_query[0][0],my_item_query[0][2],))
    conn.commit()

    data={
        "user_id":my_user_query[0][0],
        "cost":my_item_query[0][2]
    }

    producer.send(
        ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )
    time.sleep(3)
    print(f"Done sending...{i}")


print("Sending is over!")
time.sleep(10)