import numpy as np

from utils import Camera, Viewpoint, CanvasToViewpoint, Canvas, Scene, TraceRay, Sphere, COLOR_BLACK, COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLO, AmbientLight, PointLight, DirectionalLight


def main():
    camera = Camera()
    viewpoint = Viewpoint(1, 1, 1)
    canvas = Canvas(600, 600)

    scene = Scene(COLOR_BLACK, [
        Sphere(np.array([0, -1, 3]), 1, COLOR_RED),
        Sphere(np.array([2, 0, 4]), 1, COLOR_BLUE),
        Sphere(np.array([-2, 0, 4]), 1, COLOR_GREEN),
        Sphere(np.array([0, -5001, 0]), 5000, COLOR_YELLO)
    ], [
        AmbientLight(0.4),
        PointLight(0.6, np.array([2, 1, 0])),
        DirectionalLight(0.6, np.array([1, 4, 4]))
    ])

    for canvasX, canvasY in canvas.GenerateCoordinates():
        viewpointCoord = CanvasToViewpoint(canvas, viewpoint, canvasX, canvasY)
        cameraPosition = camera.GetPosition()

        color = TraceRay(scene, cameraPosition, viewpointCoord, 1, np.inf)
        canvas.PutPixel(canvasX, canvasY, color)

    canvas.SaveFigure("basic.png")


if __name__ == "__main__":
    main()
