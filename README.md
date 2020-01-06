# Performance latency test service
This service will read all the activity logged on the kafka topic (checked-application-logs). It will calculated the time spent for each check and write it to a CSV file for generating statistics and data analysis.

The separator used is a semicolon ;