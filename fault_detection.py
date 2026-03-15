def detect_faults(data):

    faults = []

    for value in data:

        if value < 10 or value > 100:

            faults.append(value)

    return faults