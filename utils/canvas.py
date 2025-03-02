import numpy as np
import matplotlib.pyplot as plt


class Canvas:
    def __init__(self, width, height):
        self.m_width = width
        self.m_height = height
        self.m_canvas = None

    def PutPixel(self, canvasX, canvasY, color):
        screenX, screenY = self.CanvasToScreen(canvasX, canvasY)
        self.m_canvas[screenY, screenX, :] = color

    def CanvasToScreen(self, canvasX, canvasY):
        screenX = self.m_width / 2 + canvasX
        screenY = self.m_height / 2 - canvasY
        return int(screenX), int(screenY)

    def ScreenToCanvas(self, coordinates):
        transMatrix = np.array([
            [1,                 0,                  0],
            [0,                 -1,                 0],
            [-self.m_width / 2, self.m_height / 2,  1]
        ], dtype=coordinates.dtype)
        return np.matmul(coordinates, transMatrix)

    def GenerateCoordinates(self):
        rowIdx, colIdx = np.indices([self.m_height, self.m_width])
        coordinates = np.stack((rowIdx, colIdx), axis=-1)
        coordinates = coordinates.reshape(-1, 2)
        homogeneous_coordinates = np.hstack((coordinates, np.ones((coordinates.shape[0], 1), dtype=coordinates.dtype)))
        return self.ScreenToCanvas(homogeneous_coordinates)

    def GetShape(self):
        return self.m_width, self.m_height

    def normalize_image(self):
        self.m_canvas[self.m_canvas > 1] = 1

    def SaveFigure(self, colors, file_name):
        self.m_canvas = colors.reshape((self.m_height, self.m_width, 3), order='F')
        self.normalize_image()

        plt.imshow(self.m_canvas)
        plt.savefig(file_name)
        plt.show()
