import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
import psycopg2

conn = psycopg2.connect(user="postgres",
                        password="k7147bdz0.",
                        host="localhost",
                        port="5432",
                        database="postgres")
cur=conn.cursor()

ORDER_KAFKA_TOPIC="order_details"
ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"


consumer=KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)
producer=KafkaProducer(
    bootstrap_servers="localhost:9092"
)

print("Gonna start listening")


while True:

    for message in consumer:
        print("Ongoing transactions")
        cosumed_message=json.loads(message.value.decode())
        print(cosumed_message)

        user_id=cosumed_message["user_id"]
        cost = cosumed_message["cost"]

        cur.execute("INSERT INTO mail (mail_id) VALUES ( %s )",(user_id,))
        conn.commit()


        print("Successful Transactions...")

        data={"customer_email":user_id}

        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )
