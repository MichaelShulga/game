from math import radians, sin, atan, degrees, sqrt, tan

from geometry import arc_angle, circle_point, circle_center, line_point


class Car:
    pos = (0, 0)
    angle = 0
    speed = 0
    wheels_angle = 0

    def __init__(self, length, width):
        self.length, self.width = length, width

    def move(self, delta):
        distance = delta * self.speed

        if self.wheels_angle:
            self.rotational_move(distance)
        else:
            self.direct_move(distance)

    def rotational_move(self, distance):
        radius = self.length / (2 * sin(radians(self.wheels_angle)))
        angle_before = self.angle + self.wheels_angle - 90  # angle between axis, rotation center and car pos before move
        distance_angle = degrees(arc_angle(distance, radius))
        angle_after = distance_angle + angle_before  # angle between axis, rotation center and car pos after move
        center = circle_center(self.pos, radians(angle_before), radius)

        self.pos = circle_point(center, radians(angle_after), radius)
        self.angle = (self.angle + distance_angle) % 360

    def direct_move(self, distance):
        self.pos = line_point(self.pos, radians(self.angle), distance)

    def get_wheels_angle(self):
        if self.wheels_angle:
            shift = self.length / (2 * tan(radians(self.wheels_angle)))

            left = degrees(atan(self.length / (shift - self.width / 2)))
            right = degrees(atan(self.length / (shift + self.width / 2)))
        else:
            left = 0
            right = 0
        return left, right
