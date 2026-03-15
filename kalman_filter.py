class KalmanFilter:

    def __init__(self, process_variance=1e-5, measurement_variance=1):

        self.process_variance = process_variance
        self.measurement_variance = measurement_variance

        self.estimate = 0
        self.error_estimate = 1

    def update(self, measurement):

        kalman_gain = self.error_estimate / (self.error_estimate + self.measurement_variance)

        self.estimate = self.estimate + kalman_gain * (measurement - self.estimate)

        self.error_estimate = (1 - kalman_gain) * self.error_estimate + abs(self.estimate - measurement) * self.process_variance

        return self.estimate