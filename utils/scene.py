import numpy as np


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

    def GetLights(self):
        for light in self.m_lights:
            yield light
