import numpy as np

from .lights import ComputeLighting, ReflectiveRay
from .models import Ray, ClosestIntersection
from .scene import Scene


def TraceRay(scene: Scene, cameraPosition, vectorView, t_min, t_max, recursionDepth):
    viewRay = Ray(cameraPosition, vectorView)
    closestSphere, closestT = ClosestIntersection(scene, viewRay, t_min, t_max)
    if closestSphere == None:
        return scene.GetBackgroundColor()

    intersectPoint = cameraPosition + closestT * vectorView
    intersectNormal = intersectPoint - closestSphere.GetCenter()
    intersectNormal = intersectNormal / np.linalg.norm(intersectNormal)

    localColor = closestSphere.GetColor() * ComputeLighting(scene, intersectPoint, intersectNormal, -vectorView, closestSphere.GetSpecular())

    reflective = closestSphere.GetReflective()
    if recursionDepth <= 0 or reflective <= 0:
        return localColor

    vectorReflective = ReflectiveRay(-vectorView, intersectNormal)
    reflectiveColor = TraceRay(scene, intersectPoint, vectorReflective, 0.001, np.inf, recursionDepth - 1)

    return localColor * (1 - reflective) + reflectiveColor * reflective
