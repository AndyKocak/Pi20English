from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
import cv2

class simplifiedPiCam:

    def __init__(self, resolution=(640, 480)):

        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.absoluteSquare = PiRGBArray(self.camera, size=self.camera.resolution)
        self.feed = self.camera.capture_continuous(self.hamKare, format="bgr", use_video_port=True)
        self.curreentSquare = None

        self.shownInSquare = dict()
        self.cameraActive = False

    def startReadingValues(self):

        Thread(target=self.__updateValues__, args=()).start()
        return self

    def __updateValues__(self):

        for f in self.feed:

            self.currentSquare = f.array
            self.absoluteSquare.truncate(0)

    def readValues(self):

        return self.currentSquare

    def showSquare(self, nameOfFrame="frame", shownDisplay=None):
        if shownDisplay is None:
            self.shownInSquare[nameOfFrame] = self.currentSquare
        else:
            self.shownInSquare[nameOfFrame] = shownDisplay

        if not self.cameraActive:
            Thread(target=self.__updateFrame__, args=()).start()

    def __updateFrame__(self):

        self.cameraActive = True

        while True:

            for name in self.shownInSquare.copy():
                cv2.imshow(name, self.shownInSquare[name])

            key = cv2.waitKey(1)

            if key == ord("q"):
                cv2.destroyAllWindows()
                break
