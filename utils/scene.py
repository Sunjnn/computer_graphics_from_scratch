import numpy as np


class Scene:
    def __init__(self, backgroundColor, spheres=[]):
        self.m_spheres = spheres
        self.m_backgroundColor = backgroundColor

    def GetSpheres(self):
        for sphere in self.m_spheres:
            yield sphere

    def GetBackgroundColor(self):
        return self.m_backgroundColor
