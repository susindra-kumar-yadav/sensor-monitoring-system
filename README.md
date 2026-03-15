# Real-Time Sensor Signal Processing System

## Overview

This project simulates a **sensor signal processing pipeline** similar to what is used in embedded systems and VLSI-based hardware monitoring.

The system generates sensor readings, filters noise, detects faulty readings, visualizes the signal, and logs the data for analysis.

The goal of this project is to demonstrate **digital signal preprocessing techniques used in hardware systems**.

---

## Features

• Sensor data simulation
• Duplicate sensor reading removal
• Moving average noise filtering
• Automatic fault injection
• Fault detection
• Real-time signal visualization
• CSV data logging for analysis

---

## Technologies Used

* Python
* NumPy
* Matplotlib

Libraries used:

* **NumPy**
* **Matplotlib**

---

## System Architecture

Sensor → Fault Injection → Digital Filter → Fault Detection → Visualization → Data Logging

This architecture mimics how embedded sensor monitoring systems process signals before storing or transmitting them.

---

## Project Structure

```
sensor_duplicate_filter
│
├── sensor_simulator.py
├── digital_filter.py
├── fault_detection.py
├── visualization.py
├── realtime_monitor.py
├── data_logger.py
├── export_data.py
├── main.py
│
├── sensor_log.csv
├── filtered_sensor_data.csv
│
└── README.md
```

---

## Installation

Install required Python libraries:

```
pip install numpy matplotlib
```

---

## Running the Offline Processing Pipeline

Run the command:

```
python main.py
```

This will:

1. Generate sensor data
2. Remove duplicate readings
3. Apply moving average filtering
4. Detect faulty readings
5. Visualize the processed signal
6. Export filtered data to CSV

---

## Running the Real-Time Monitoring System

Run:

```
python realtime_monitor.py
```

The system will:

• simulate live sensor data
• inject random sensor faults
• apply noise filtering
• detect anomalies
• display a real-time graph
• store readings in a CSV log file

---

## Example Output

The system produces a real-time graph showing:

* Raw sensor data
* Filtered signal
* Faulty readings highlighted

Logged data example:

```
timestamp,value,status
2026-03-15 12:01:10,29.4,NORMAL
2026-03-15 12:01:11,120,FAULT
2026-03-15 12:01:12,30.1,NORMAL
```

---

## Applications

This type of system is commonly used in:

• Embedded sensor monitoring
• Industrial IoT systems
• Hardware signal preprocessing
• Data acquisition systems

---

## Future Improvements

Possible upgrades:

• Real-time dashboard UI
• Advanced signal filtering algorithms
• Sensor network simulation
• Machine learning based anomaly detection

---

## Author

Project developed as a **sensor signal processing simulation for embedded systems learning**.
