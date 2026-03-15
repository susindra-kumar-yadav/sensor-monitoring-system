import pandas as pd

def save_to_csv(data):

    df = pd.DataFrame(data, columns=["Sensor Data"])

    df.to_csv("filtered_sensor_data.csv", index=False)