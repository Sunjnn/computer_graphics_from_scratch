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
    def __init__(self, center, radius, color, specular, reflective):
        self.m_center = center
        self.m_radius = radius
        self.m_color = color
        self.m_specular = specular
        self.m_reflective = reflective

    def GetCenter(self):
        return self.m_center

    def GetRadius(self):
        return self.m_radius

    def GetColor(self):
        return self.m_color

    def GetSpecular(self):
        return self.m_specular

    def GetReflective(self):
        return self.m_reflective


def IntersectRaySphere(rayDirections, raySources, sphere: Sphere):
    As = np.sum(rayDirections * rayDirections, axis=1)

    sphereCenter = sphere.GetCenter()
    vectorCOs = raySources - sphereCenter
    Bs = 2 * np.sum(vectorCOs * rayDirections, axis=1)

    sphereRadius = sphere.GetRadius()
    Cs = np.sum(vectorCOs * vectorCOs) - sphereRadius * sphereRadius

    deltas = Bs * Bs - 4 * As * Cs
    rootNums = np.zeros(deltas.shape, dtype=np.int32)
    rootNums[deltas == 0] = 1
    rootNums[deltas > 0]  = 2

    deltas[deltas < 0] = 0.0
    twiceAs = 2 * As
    sqrtDeltas = np.sqrt(deltas)
    root1 = (-Bs - sqrtDeltas) / twiceAs
    root2 = (-Bs + sqrtDeltas) / twiceAs
    root1[root2 < root1] = root2[root2 < root1]

    return rootNums, root1
