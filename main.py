from sensor_simulator import generate_sensor_data
from digital_filter import remove_duplicates, moving_average
from fault_detection import detect_faults
from visualization import plot_data
from export_data import save_to_csv

sensor_data = generate_sensor_data()

unique_data = remove_duplicates(sensor_data)

filtered_data = moving_average(unique_data)

faults = detect_faults(filtered_data)

print("Faulty readings:", faults)
plot_data(sensor_data, filtered_data, faults)

save_to_csv(filtered_data)