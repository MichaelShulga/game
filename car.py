from math import radians, sin, cos, pi, asin, degrees


class Car:
    pos = (0, 0)
    angle = 0
    speed = 0
    wheels_angle = 0

    def __init__(self, length, width):
        self.length, self.width = length, width

    def get_radius(self):
        return self.length / (2 * sin(radians(self.wheels_angle)))

    def get_center(self, radius, shift=False):
        general = self.angle + self.wheels_angle - 90  # angle between axis and car pos

        center = (-radius * cos(radians(general)),
                  radius * sin(radians(general)))  # center without current pos shift
        """минус по Oy из-за специфичного расположения осей в pygame"""
        if shift:
            center = (center[0] + self.pos[0],
                      center[1] + self.pos[1])

        return center

    def get_distance(self, delta):
        return delta * self.speed

    def get_distance_angle(self, distance, radius):
        return distance / (2 * pi * radius) * 360

    def

    def move(self, delta):
        print(f"pos: {self.pos}")
        # distance traveled by the car
        distance = delta * self.speed

        if not self.wheels_angle:
            pass

        # radius of center of rotation
        r = self.length / (2 * sin(radians(self.wheels_angle)))

        # center of rotation
        general = self.angle + self.wheels_angle - 90  # angle between axis and car pos
        center = (-r * cos(radians(general)),
                  r * sin(radians(general)))  # center without current pos shift
        """минус по Oy из-за специфичного расположения осей в pygame"""

        # angle between 0 and point to which we are going to move
        distance_angle = distance / (2 * pi * r) * 360
        shift_angle = degrees(asin(
            (-center[1]) / r))

        angle = distance_angle - shift_angle

        shift_x = (cos(radians(angle)) - cos(radians(-shift_angle))) * r
        shift_y = -(sin(radians(angle)) - sin(radians(-shift_angle))) * r

        print(shift_x)
        print(shift_y)
        self.pos = (shift_x + self.pos[0],
                    shift_y + self.pos[1])
        self.angle = (self.angle + distance_angle) % 360
        # print(f"r: {r}")
        # print(f"move_angle: {angle}, distance_angle: {distance_angle}б, shift_angle: {shift_angle}")
        # print(f"distance: {distance}")
        print(f"center: {center}")
        # print(f"general: {general}")
        print(f"angle: {self.angle}")

    def rotation_center(self):
        r = self.length / (2 * sin(radians(self.wheels_angle)))
        # center of rotation
        general = self.angle + self.wheels_angle - 90  # angle between axis and car pos
        center = (-r * cos(radians(general) + self.pos[0]),
                  r * sin(radians(general)) + self.pos[1])  # center without current pos shift
        """минус по Oy из-за специфичного расположения осей в pygame"""
        return center
