import numpy as np



class Light:
    def __init__(self, intensity):
        self.m_intensity = intensity

    def ComputeLighting(self, point, normal):
        return self.m_intensity


def DiffuseReflection(intensity, vectorLight, normal):
    dotNormalLight = np.dot(normal, vectorLight)
    if dotNormalLight <= 0:
        return 0
    normNormal = np.linalg.norm(normal)
    normLight = np.linalg.norm(vectorLight)
    return intensity * dotNormalLight / normNormal / normLight


class PointLight(Light):
    def __init__(self, intensity, position):
        super().__init__(intensity)
        self.m_position = position

    def ComputeLighting(self, point, normal):
        vectorLight = self.m_position - point
        return DiffuseReflection(self.m_intensity, vectorLight, normal)


class DirectionalLight(Light):
    def __init__(self, intensity, direction):
        super().__init__(intensity)
        self.m_direction = direction

    def ComputeLighting(self, point, normal):
        vectorLight = self.m_direction
        return DiffuseReflection(self.m_intensity, vectorLight, normal)


AmbientLight = Light


def ComputeLighting(point, normal, lights: list[Light]):
    intensity = 0
    for light in lights:
        intensity += light.ComputeLighting(point, normal)
    return intensity
