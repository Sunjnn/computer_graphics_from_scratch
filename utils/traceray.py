import numpy as np

from .lights import ComputeLighting, ReflectiveRay
from .scene import Scene, ClosestIntersection


def TraceRay(scene: Scene, colorShape, cameraPosition, vectorViews, t_min, t_max, recursionDepth):
    closestSpheres, closestTs = ClosestIntersection(scene, vectorViews, cameraPosition, t_min, t_max)
    closestTs = closestTs.reshape(-1, 1)

    intersectPoints = cameraPosition + closestTs * vectorViews
    intersectNormals = intersectPoints - scene.GetSphereCenters(closestSpheres)
    intersectNormals = intersectNormals / np.linalg.norm(intersectNormals, axis=1, keepdims=True)

    sphereColors = scene.GetColors(closestSpheres)
    sphereColors[closestSpheres == -1] = scene.GetBackgroundColor()

    localColors = sphereColors * ComputeLighting(scene, intersectPoints, intersectNormals, -vectorViews, scene.GetSpeculars(closestSpheres)).reshape(-1, 1)

    if recursionDepth <= 0:
        return localColors

    reflectives = scene.GetReflectives(closestSpheres)
    reflectives[reflectives <= 0] = 0

    vectorReflectives = ReflectiveRay(-vectorViews, intersectNormals)
    reflectiveColors = TraceRay(scene, colorShape, intersectPoints, vectorReflectives, 0.001, np.inf, recursionDepth - 1)

    return localColors * (1 - reflectives).reshape(-1, 1) + reflectiveColors * reflectives.reshape(-1, 1)
