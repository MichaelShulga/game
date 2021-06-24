from math import radians, sin, cos, pi, asin, degrees

from geometry import arc_angle, circle_point, circle_center


class Car:
    pos = (0, 0)
    angle = 0
    speed = 0
    wheels_angle = 0

    def __init__(self, length, width):
        self.length, self.width = length, width

    def get_radius(self):
        return self.length / (2 * sin(radians(self.wheels_angle)))

    def get_distance(self, delta):
        return delta * self.speed

    def move(self, delta):
        distance = self.get_distance(delta)
        r = self.get_radius()
        angle_before = self.angle + self.wheels_angle - 90  # angle between axis and car pos before move
        distance_angle = degrees(arc_angle(distance, r))
        angle_after = distance_angle + angle_before
        center = circle_center(self.pos, radians(angle_before), r)

        self.pos = circle_point(center, radians(angle_after), r)
        self.angle = (self.angle + distance_angle) % 360
