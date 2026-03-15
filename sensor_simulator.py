import numpy as np

def generate_sensor_data():

    data = np.random.normal(30, 2, 50)

    duplicates = data[:5]

    sensor_data = np.concatenate((data, duplicates))

    # Add faulty sensor readings
    sensor_data[10] = 120
    sensor_data[20] = -5

    return sensor_data