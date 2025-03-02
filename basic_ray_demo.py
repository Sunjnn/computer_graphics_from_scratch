import numpy as np

from utils import Camera, Viewpoint, CanvasToViewpoint, Canvas, Scene, TraceRay, Sphere, COLOR_BLACK, COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLO, AmbientLight, PointLight, DirectionalLight


def main():
    camera = Camera()
    viewpoint = Viewpoint(1, 1, 1)
    canvas = Canvas(600, 600)

    scene = Scene(COLOR_BLACK, [
        Sphere(np.array([0, -1, 3, 1]), 1, COLOR_RED, 500, 0.2),
        Sphere(np.array([2, 0, 4, 1]), 1, COLOR_BLUE, 500, 0.3),
        Sphere(np.array([-2, 0, 4, 1]), 1, COLOR_GREEN, 10, 0.4),
        Sphere(np.array([0, -5001, 0, 1]), 5000, COLOR_YELLO, 1000, 0.5)
    ], [
        AmbientLight(0.2),
        PointLight(0.6, np.array([2, 1, 0, 1])),
        DirectionalLight(0.2, np.array([1, 4, 4, 0]))
    ])

    canvasCoordinates = canvas.GenerateCoordinates()
    viewpointCoordinates = CanvasToViewpoint(canvas, viewpoint, canvasCoordinates)
    cameraPosition = camera.GetPosition()

    colors = TraceRay(scene, [canvas.m_height, canvas.m_width, 3], cameraPosition, viewpointCoordinates - cameraPosition, 1, np.inf, 3)

    canvas.SaveFigure(colors, "basic.png")


if __name__ == "__main__":
    main()
