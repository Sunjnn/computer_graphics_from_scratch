import numpy as np


class Ray:
    def __init__(self, source, direction):
        self.m_direction = direction
        self.m_source = source

    def GetPoint(self, t):
        return self.m_source + t * self.m_direction

    def GetDirection(self):
        return self.m_direction

    def GetSource(self):
        return self.m_source


class Sphere:
    def __init__(self, center, radius, color):
        self.m_center = center
        self.m_radius = radius
        self.m_color = color

    def GetCenter(self):
        return self.m_center

    def GetRadius(self):
        return self.m_radius

    def GetColor(self):
        return self.m_color


def IntersectRaySphere(ray: Ray, sphere: Sphere):
    rayDirection = ray.GetDirection()
    a = np.dot(rayDirection, rayDirection)

    raySource = ray.GetSource()
    sphereCenter = sphere.GetCenter()
    vectorCO = raySource - sphereCenter
    b = 2 * np.dot(vectorCO, rayDirection)

    sphereRadius = sphere.GetRadius()
    c = np.dot(vectorCO, vectorCO) - sphereRadius * sphereRadius

    delta = b * b - 4 * a * c
    if delta < 0:
        return "No root", []
    elif delta == 0:
        root = -b / 2 / a
        return "One root", [root]
    else:
        delta_sqrt = np.sqrt(delta)
        root1 = (-b + delta_sqrt) / 2 / a
        root2 = (-b - delta_sqrt) / 2 / a
        return "Two root", [root1, root2]
