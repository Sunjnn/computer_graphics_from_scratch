import numpy as np
import matplotlib.pyplot as plt


class Canvas:
    def __init__(self, width, height):
        self.m_width = width
        self.m_height = height
        self.m_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    def PutPixel(self, canvasX, canvasY, color):
        screenX, screenY = self.CanvasToScreen(canvasX, canvasY)
        self.m_canvas[screenY, screenX, :] = color

    def CanvasToScreen(self, canvasX, canvasY):
        screenX = self.m_width / 2 + canvasX
        screenY = self.m_height / 2 - canvasY
        return int(screenX), int(screenY)

    def ScreenToCanvas(self, screenX, screenY):
        canvasX = screenX - self.m_width / 2
        canvasY = self.m_height / 2 - screenY
        return int(canvasX), int(canvasY)

    def GenerateCoordinates(self):
        for x in range(self.m_width):
            for y in range(self.m_height):
                yield self.ScreenToCanvas(x, y)

    def GetShape(self):
        return self.m_width, self.m_height

    def SaveFigure(self, file_name):
        plt.imshow(self.m_canvas)
        plt.savefig(file_name)
        plt.show()
