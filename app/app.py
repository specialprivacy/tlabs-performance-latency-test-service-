import sys
import uuid
from kafka import KafkaConsumer
from json import dumps
from json import loads

consumer = KafkaConsumer(
  "checked-application-logs",
  bootstrap_servers=['kafka:9092'],
  auto_offset_reset='earliest',
  enable_auto_commit=True,
  group_id=str(uuid.uuid4()),
  value_deserializer=lambda x: loads(x.decode('utf-8')))

print("starting to write...")
f= open("/logs/logs","w+")

for message in consumer:
  message = message.value
  # print(str(message))
  message_id = message["eventID"]
  time_stamp = float(message["timestamp"])
  checked_time_stamp = float(message["checkedTimestamp"])
  time_spent = abs(time_stamp - checked_time_stamp)
  log_message = str(message_id) + ";" + str(time_stamp) + ";" + str(checked_time_stamp) + ";" + str(time_spent)
  f.write(log_message)

f.close()
