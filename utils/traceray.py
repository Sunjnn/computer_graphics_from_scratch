import numpy as np

from .models import Ray, Sphere, IntersectRaySphere
from .scene import Scene


def TraceRay(scene: Scene, cameraPosition, viewpointCoord, t_min, t_max):
    closestT = np.inf
    closestSphere: Sphere = None

    vectorView = viewpointCoord - cameraPosition
    viewRay = Ray(cameraPosition, vectorView)

    for sphere in scene.GetSpheres():
        rootStr, roots = IntersectRaySphere(viewRay, sphere)
        if rootStr != "No root":
            for root in roots:
                if root >= t_min and root < t_max and root < closestT:
                    closestT = root
                    closestSphere = sphere

    if closestT == np.inf:
        return scene.GetBackgroundColor()

    intersectPoint = cameraPosition + closestT * vectorView
    intersectNormal = intersectPoint - closestSphere.GetCenter()
    return closestSphere.GetColor() * scene.ComputeLighting(intersectPoint, intersectNormal)
