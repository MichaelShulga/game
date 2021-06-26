from math import cos, sin

from config import X_INVERSION, Y_INVERSION

"""
RADIANS STANDARD
"""


def arc_angle(arc, radius):
    return arc / radius


def circle_center(point, angle, radius):
    shifted_center = (-radius * cos(angle) * X_INVERSION,
                      -radius * sin(angle) * Y_INVERSION)  # point offset

    center = (shifted_center[0] + point[0],
              shifted_center[1] + point[1])

    return center


def circle_point(center, angle, radius):
    shifted_point = (radius * cos(angle) * X_INVERSION,
                     radius * sin(angle) * Y_INVERSION)  # point offset

    point = (shifted_point[0] + center[0],
             shifted_point[1] + center[1])

    return point


def line_point(point, angle, distance):
    shifted_point = (distance * cos(angle) * X_INVERSION,
                     distance * sin(angle) * Y_INVERSION)  # point offset

    point = (shifted_point[0] + point[0],
             shifted_point[1] + point[1])

    return point
