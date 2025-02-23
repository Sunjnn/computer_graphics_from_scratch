import numpy as np



class Light:
    def __init__(self, intensity):
        self.m_intensity = intensity

    def ComputeLighting(self, point, normal, vectorView, specular):
        return self.m_intensity


def DiffuseReflection(intensity, vectorLight, normal):
    dotNormalLight = np.dot(normal, vectorLight)
    if dotNormalLight <= 0:
        return 0
    normNormal = np.linalg.norm(normal)
    normLight = np.linalg.norm(vectorLight)
    return intensity * dotNormalLight / normNormal / normLight


def SpecularReflection(intensity, vectorLight, normal, vectorView, specular):
    if specular == -1:
        return 0

    vectorReflectLight = 2 * normal * np.dot(normal, vectorLight) - vectorLight
    dotReflectView = np.dot(vectorReflectLight, vectorView)
    if dotReflectView <= 0:
        return 0

    normReflect = np.linalg.norm(vectorReflectLight)
    normView = np.linalg.norm(vectorView)

    return intensity * np.pow(dotReflectView / normReflect / normView, specular)


class PointLight(Light):
    def __init__(self, intensity, position):
        super().__init__(intensity)
        self.m_position = position

    def ComputeLighting(self, point, normal, vectorView, specular):
        vectorLight = self.m_position - point
        diffuseIntensity = DiffuseReflection(self.m_intensity, vectorLight, normal)
        specularIntensity = SpecularReflection(self.m_intensity, vectorLight, normal, vectorView, specular)
        return diffuseIntensity + specularIntensity


class DirectionalLight(Light):
    def __init__(self, intensity, direction):
        super().__init__(intensity)
        self.m_direction = direction

    def ComputeLighting(self, point, normal, vectorView, specular):
        vectorLight = self.m_direction
        diffuseIntensity = DiffuseReflection(self.m_intensity, vectorLight, normal)
        specularIntensity = SpecularReflection(self.m_intensity, vectorLight, normal, vectorView, specular)
        return diffuseIntensity + specularIntensity


AmbientLight = Light


def ComputeLighting(point, normal, vectorView, specular, lights: list[Light]):
    intensity = 0
    for light in lights:
        intensity += light.ComputeLighting(point, normal, vectorView, specular)
    return intensity
