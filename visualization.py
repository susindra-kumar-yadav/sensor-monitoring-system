import matplotlib.pyplot as plt

def plot_data(raw, filtered, faults):

    plt.plot(raw, label="Raw Data")

    plt.plot(filtered, label="Filtered Data")

    if faults:
        fault_x = []
        fault_y = []

        for i, value in enumerate(filtered):
            if value in faults:
                fault_x.append(i)
                fault_y.append(value)

        plt.scatter(fault_x, fault_y, color='red', label="Faulty Reading")

    plt.xlabel("Samples")
    plt.ylabel("Sensor Value")

    plt.title("Sensor Signal Processing")

    plt.legend()
    plt.grid(True)

    plt.show()