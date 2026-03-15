# Real-Time Sensor Monitoring System

This project simulates a real-time sensor monitoring system used in embedded and hardware systems.

## Features
- Real-time sensor data simulation
- Moving average noise filtering
- Automatic fault injection
- Fault detection and visualization
- Live graph monitoring
- CSV data logging

## Technologies Used
Python
NumPy
Matplotlib

## System Architecture
Sensor → Fault Injection → Digital Filter → Fault Detection → Visualization → Data Logging

## How to Run

Install dependencies:

pip install numpy matplotlib

Run the system:

python realtime_monitor.py

## Output

The system shows:
- Live sensor graph
- Fault detection markers
- CSV log of sensor data

Example CSV output:

timestamp,value,status
2026-03-15 12:01:10,29.4,NORMAL
2026-03-15 12:01:11,120,FAULT