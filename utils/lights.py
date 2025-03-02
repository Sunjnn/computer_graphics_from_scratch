import numpy as np

from .models import Ray
from .scene import Scene, ClosestIntersection


class Light:
    def __init__(self, intensity):
        self.m_intensity = intensity

    def ComputeLighting(self, scene, points, normals, vectorViews, speculars):
        return self.m_intensity


def DiffuseReflection(intensity, vectorLights, normals):
    dotNormalLights = np.sum(normals * vectorLights, axis=1)
    intensitys = np.full([vectorLights.shape[0]], intensity)
    intensitys[dotNormalLights <= 0] = 0

    normNormals = np.linalg.norm(normals, axis=1)
    normLights = np.linalg.norm(vectorLights, axis=1)
    return intensitys * dotNormalLights / normNormals / normLights


def ReflectiveRay(vectorLights, normals):
    vectorReflectLights = 2 * normals * np.sum(normals * vectorLights, axis=1, keepdims=True) - vectorLights
    return vectorReflectLights


def SpecularReflection(intensity, vectorLights, normals, vectorViews, speculars):
    intensity = np.full([vectorLights.shape[0]], intensity)
    intensity[speculars == -1] = 0

    vectorReflectLights = ReflectiveRay(vectorLights, normals)
    dotReflectViews = np.sum(vectorReflectLights * vectorViews, axis=1)
    dotReflectViews[dotReflectViews <= 0] = 0

    normReflects = np.linalg.norm(vectorReflectLights, axis=1)
    normViews = np.linalg.norm(vectorViews, axis=1)

    return intensity * np.pow(dotReflectViews / normReflects / normViews, speculars)


class PointLight(Light):
    def __init__(self, intensity, position):
        super().__init__(intensity)
        self.m_position = position

    def ComputeLighting(self, scene, points, normals, vectorViews, speculars):
        vectorLights = self.m_position - points

        t_max = 1
        shadowSpheres, shadowTs = ClosestIntersection(scene, vectorLights, points, 0.001, t_max)

        diffuseIntensitys = DiffuseReflection(self.m_intensity, vectorLights, normals)
        specularIntensitys = SpecularReflection(self.m_intensity, vectorLights, normals, vectorViews, speculars)

        intensitys = diffuseIntensitys + specularIntensitys
        intensitys[shadowSpheres == -1] = 0

        return intensitys


class DirectionalLight(Light):
    def __init__(self, intensity, direction):
        super().__init__(intensity)
        self.m_direction = direction

    def ComputeLighting(self, scene, points, normals, vectorViews, speculars):
        vectorLights = np.broadcast_to(self.m_direction, points.shape)

        t_max = np.inf
        shadowSphere, shadowT = ClosestIntersection(scene, vectorLights, points, 0.001, t_max)

        diffuseIntensitys = DiffuseReflection(self.m_intensity, vectorLights, normals)
        specularIntensitys = SpecularReflection(self.m_intensity, vectorLights, normals, vectorViews, speculars)

        intensitys = diffuseIntensitys + specularIntensitys
        intensitys[shadowSphere == -1] = 0

        return intensitys


AmbientLight = Light


def ComputeLighting(scene: Scene, points, normals, vectorViews, speculars):
    intensity = 0
    for light in scene.GetLights():
        intensity += light.ComputeLighting(scene, points, normals, vectorViews, speculars)
    return intensity
