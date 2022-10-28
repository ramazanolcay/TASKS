from kafka import  KafkaConsumer
import json
import psycopg2

conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")
cur=conn.cursor()




ORDER_KAFKA_CONFIRMED_TOPIC="order_confirmed"

consumer=KafkaConsumer(
    ORDER_KAFKA_CONFIRMED_TOPIC,
    bootstrap_servers="localhost:9092"
)

email_sent_so_far=set()
print("Email is listening")

while True:
    for message in consumer:
        consumed_message=json.loads(message.value.decode())
        customer_email=consumed_message["customer_email"]

        print(f"Sending email to mail_id: {customer_email}")
        email_sent_so_far.add(customer_email)
        cur.execute("UPDATE mail set checker= (%s) WHERE mail_id=(%s)",(True,customer_email,))
        conn.commit()

        print(f"So far emails sent to :{len(email_sent_so_far)} unique emails")
