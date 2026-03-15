import streamlit as st
import pandas as pd
import time
import numpy as np

st.title("Real-Time Sensor Monitoring Dashboard")

chart = st.line_chart()

data = []

while True:

    sensor_value = np.random.normal(30, 2)

    if sensor_value > 50 or sensor_value < 10:
        status = "FAULT"
    else:
        status = "NORMAL"

    new_data = pd.DataFrame(
        {"Sensor Value": [sensor_value]}
    )

    chart.add_rows(new_data)

    st.write("Latest Sensor Value:", round(sensor_value,2))
    st.write("Status:", status)

    time.sleep(1)