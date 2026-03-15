from data_logger import log_data
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

# Moving average filter
def moving_average(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Generate normal sensor value
def generate_sensor_value():
    return np.random.normal(30, 2)

# Random fault injection
def inject_fault(value):
    if random.random() < 0.05:   # 5% chance of fault
        return random.choice([120, -10])
    return value

window = deque(maxlen=50)

plt.ion()

fig, ax = plt.subplots()

while True:

    sensor_value = generate_sensor_value()

    sensor_value = inject_fault(sensor_value)

    # Detect fault
    if sensor_value > 50 or sensor_value < 10:
        status = "FAULT"
    else:
        status = "NORMAL"

    # Save data to CSV
    log_data(sensor_value, status)

    window.append(sensor_value)

    raw_data = list(window)

    if len(raw_data) >= 5:

        filtered_data = moving_average(raw_data)

        ax.clear()

        ax.plot(raw_data, label="Raw Sensor Data")

        ax.plot(range(4, len(raw_data)), filtered_data, label="Filtered Data")

        # Fault detection markers
        fault_x = []
        fault_y = []

        for i, v in enumerate(raw_data):
            if v > 50 or v < 10:
                fault_x.append(i)
                fault_y.append(v)

        if fault_x:
            ax.scatter(fault_x, fault_y, color='red', label="Fault Detected")

        ax.set_title("Real-Time Sensor Monitoring")
        ax.set_xlabel("Samples")
        ax.set_ylabel("Sensor Value")

        ax.legend()
        ax.grid(True)

        plt.pause(0.5)