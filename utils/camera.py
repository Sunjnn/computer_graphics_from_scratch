import numpy as np

from .canvas import Canvas


class Camera:
    def __init__(self, position=np.zeros(3)):
        self.m_position = position

    def GetPosition(self):
        return self.m_position


class Viewpoint:
    def __init__(self, width, height, distance):
        self.m_width = width
        self.m_height = height
        self.m_distance = distance

    def GetShape(self):
        return self.m_width, self.m_height

    def GetDistance(self):
        return self.m_distance


def CanvasToViewpoint(canvas: Canvas, viewpoint: Viewpoint, canvasX, canvasY):
    viewpointWidth, viewpointHeight = viewpoint.GetShape()
    canvasWidth, canvasHeight = canvas.GetShape()

    viewpointX = canvasX * viewpointWidth / canvasWidth
    viewpointY = canvasY * viewpointHeight / canvasHeight
    viewpointZ = viewpoint.GetDistance()
    return np.array([viewpointX, viewpointY, viewpointZ])
