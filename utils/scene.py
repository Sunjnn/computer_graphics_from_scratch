import numpy as np

from .models import Sphere, IntersectRaySphere


class Scene:
    def __init__(self, backgroundColor, spheres=[], lights=[]):
        self.m_spheres = spheres
        self.m_backgroundColor = backgroundColor
        self.m_lights = lights

    def GetSpheres(self):
        for index, sphere in enumerate(self.m_spheres):
            yield index, sphere

    def GetBackgroundColor(self):
        return self.m_backgroundColor

    def GetSphereCenters(self, sphereIndexs):
        centers = np.array([sphere.GetCenter() for sphere in self.m_spheres])
        return centers[sphereIndexs]

    def GetColors(self, sphereIndexs):
        colors = np.array([sphere.GetColor() for sphere in self.m_spheres])
        return colors[sphereIndexs]

    def GetSpeculars(self, sphereIndexs):
        speculars = np.array([sphere.GetSpecular() for sphere in self.m_spheres])
        return speculars[sphereIndexs]

    def GetReflectives(self, sphereIndexs):
        reflectives = np.array([sphere.GetReflective() for sphere in self.m_spheres])
        return reflectives[sphereIndexs]

    def GetLights(self):
        for light in self.m_lights:
            yield light


def ClosestIntersection(scene: Scene, rayDirections, raySources, t_min, t_max):
    closestTs = np.full((rayDirections.shape[0]), np.inf)
    closestSpheres = np.full_like(closestTs, -1, dtype=np.int32)

    for sphereIndex, sphere in scene.GetSpheres():
        rootNums, roots = IntersectRaySphere(rayDirections, raySources, sphere)
        index = rootNums > 0
        index = np.logical_and(index, roots >= t_min)
        index = np.logical_and(index, roots < t_max)
        index = np.logical_and(index, roots < closestTs)

        closestTs[index] = roots[index]
        closestSpheres[index] = sphereIndex

    return closestSpheres, closestTs
