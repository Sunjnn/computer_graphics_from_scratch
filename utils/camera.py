import numpy as np

from .canvas import Canvas


class Camera:
    def __init__(self, position=np.array([0, 0, 0, 1.0])):
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


def CanvasToViewpoint(canvas: Canvas, viewpoint: Viewpoint, canvasCoordinates):
    viewpointWidth, viewpointHeight = viewpoint.GetShape()
    canvasWidth, canvasHeight = canvas.GetShape()
    projectMatrix = np.array([
        [viewpointWidth / canvasWidth, 0, 0, 0],
        [0, viewpointHeight / canvasHeight, 0, 0],
        [0, 0, viewpoint.GetDistance(), 1]
    ])
    return np.matmul(canvasCoordinates, projectMatrix)
