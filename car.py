from math import radians, sin, cos, pi, asin, degrees


class Wheels:
    def __init__(self):
        self.angle = 0  # angle of center wheel


class Car:
    pos = (0, 0)
    angle = 0
    speed = 0
    wheels = Wheels()

    def __init__(self, length, width):
        self.length, self.width = length, width

    def move(self, delta):
        print(f"pos: {self.pos}")
        # distance traveled by the car
        distance = delta * self.speed

        if not self.wheels.angle:
            pass

        # radius of center of rotation
        r = self.length / (2 * sin(radians(self.wheels.angle)))

        # center of rotation
        general = self.angle + self.wheels.angle + 90  # angle between axis and car pos
        center = (r * cos(radians(general)),
                  -r * sin(radians(general)))  # center without current pos shift
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
        r = self.length / (2 * sin(radians(self.wheels.angle)))
        # center of rotation
        general = self.angle + self.wheels.angle + 90  # angle between axis and car pos
        center = (r * cos(radians(general) + self.pos[0]),
                  -r * sin(radians(general)) + self.pos[1])  # center without current pos shift
        """минус по Oy из-за специфичного расположения осей в pygame"""
        return center

    def update(self, delta):
        self.move(delta)

    def image(self):
        pass

