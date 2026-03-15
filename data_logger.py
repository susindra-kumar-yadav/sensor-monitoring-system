import csv
from datetime import datetime

def log_data(value, status):

    with open("sensor_log.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([datetime.now(), value, status])