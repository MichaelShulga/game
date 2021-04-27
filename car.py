class Car:
    def __init__(self):
        self.x, self.y = 0, 0

        self.speed = 0  # pixels per seconds

        # acceleration parameters f(x) = a * x + b
        self.a_acceleration = 1  # a >= 1
        self.b_acceleration = 1

        # braking parameters f(x) = a * x + b
        self.a_braking = 1  # 0 < a < 1
        self.b_braking = 1

        self.acceleration_speed = 1  # pixels per seconds

        self.angle = 0  # 0-360 degree

        self.wheel_angle = 90  # 0-180 degree
        self.wheel_difference_coefficient = 1.36

    def accelerate(self, delta_time):
        self.speed = (self.speed * self.a_acceleration + self.b_acceleration) * delta_time

    def brake(self, delta_time):  # stop
        self.speed = (self.speed * self.a_acceleration - self.b_acceleration) * delta_time

    def rotation(self, delta_time, angle):
        pass

    def move(self, delta_time):
        pass
