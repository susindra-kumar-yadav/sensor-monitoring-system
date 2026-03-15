def remove_duplicates(data):

    unique_data = list(dict.fromkeys(data))

    return unique_data


def moving_average(data, window_size=3):

    filtered = []

    for i in range(len(data)):

        start = max(0, i-window_size+1)

        window = data[start:i+1]

        filtered.append(sum(window)/len(window))

    return filtered