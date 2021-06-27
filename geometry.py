from math import cos, sin

from config import X_INVERSION, Y_INVERSION

"""
RADIANS STANDARD
"""


def arc_angle(arc, radius):
    return arc / radius


def shift_by_angle(angle, line):  # point offset
    return (line * cos(angle) * X_INVERSION,
            line * sin(angle) * Y_INVERSION)


def circle_center(point, angle, radius):
    shifted_center = shift_by_angle(angle, radius)
    return (point[0] - shifted_center[0],
            point[1] - shifted_center[1])


def circle_point(center, angle, radius):
    shifted_point = shift_by_angle(angle, radius)
    return (center[0] + shifted_point[0],
            center[1] + shifted_point[1])


def line_point(point, angle, distance):
    shifted_point = shift_by_angle(angle, distance)
    return (shifted_point[0] + point[0],
            shifted_point[1] + point[1])
