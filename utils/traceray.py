import numpy as np

from .lights import ComputeLighting
from .models import Ray, ClosestIntersection
from .scene import Scene


def TraceRay(scene: Scene, cameraPosition, viewpointCoord, t_min, t_max):
    vectorView = viewpointCoord - cameraPosition
    viewRay = Ray(cameraPosition, vectorView)
    closestSphere, closestT = ClosestIntersection(scene, viewRay, t_min, t_max)
    if closestSphere == None:
        return scene.GetBackgroundColor()

    intersectPoint = cameraPosition + closestT * vectorView
    intersectNormal = intersectPoint - closestSphere.GetCenter()
    intersectNormal = intersectNormal / np.linalg.norm(intersectNormal)

    return closestSphere.GetColor() * ComputeLighting(scene, intersectPoint, intersectNormal, -vectorView, closestSphere.GetSpecular())
