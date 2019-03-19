from kafka import KafkaConsumer

consumer = KafkaConsumer(
  "checked-application-logs",
  bootstrap_servers=['kafka:9092'],
  auto_offset_reset='earliest',
  enable_auto_commit=True,
  group_id=str(uuid.uuid4()),
  value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
  message = message.value
  if message["eventID"] == event_id:
    message_id = message["eventID"]
    time_stamp = long(message["timestamp"])
    checked_time_stamp = long(message["checkedTimestamp"])
    time_spent = abs(time_stamp - checked_time_stamp)
    print(str(message_id) + ";" + str(time_stamp) + ";" + str(checked_time_stamp) + ";" + str(time_spent))
