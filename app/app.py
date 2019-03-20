import sys
from kafka import KafkaConsumer
from json import dumps
from json import loads

print("creating")
consumer = KafkaConsumer(
  "checked-application-logs",
  bootstrap_servers=['kafka:9092'],
  auto_offset_reset='earliest',
  enable_auto_commit=True,
  group_id="12345678",
  value_deserializer=lambda x: loads(x.decode('utf-8')))

print("reading")
sys.stdout.flush()

for message in consumer:
  message = message.value
  # print(str(message))
  message_id = message["eventID"]
  time_stamp = float(message["timestamp"])
  checked_time_stamp = float(message["checkedTimestamp"])
  time_spent = abs(time_stamp - checked_time_stamp)
  print(str(message_id) + ";" + str(time_stamp) + ";" + str(checked_time_stamp) + ";" + str(time_spent))
  sys.stdout.flush()
