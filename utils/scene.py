import numpy as np

from .lights import ComputeLighting


class Scene:
    def __init__(self, backgroundColor, spheres=[], lights=[]):
        self.m_spheres = spheres
        self.m_backgroundColor = backgroundColor
        self.m_lights = lights

    def GetSpheres(self):
        for sphere in self.m_spheres:
            yield sphere

    def GetBackgroundColor(self):
        return self.m_backgroundColor

    def ComputeLighting(self, point, normal):
        return ComputeLighting(point, normal, self.m_lights)
