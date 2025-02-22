import numpy as np

from .models import Ray, IntersectRaySphere
from .scene import Scene


def TraceRay(scene: Scene, cameraPosition, viewpointCoord, t_min, t_max):
    closest_t = np.inf
    color = scene.GetBackgroundColor()
    for sphere in scene.GetSpheres():
        viewRay = Ray(cameraPosition, viewpointCoord)
        rootStr, roots = IntersectRaySphere(viewRay, sphere)
        if rootStr != "No root":
            for root in roots:
                if root >= t_min and root < t_max and root < closest_t:
                    closest_t = root
                    color = sphere.GetColor()

    return color
