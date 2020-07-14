import pygame
from threading import Thread


class Controller:

    def __init__(self):

        pygame.init()

        pygame.joystick.init()

        self.j = pygame.joystick.Joystick(0)
        self.j.init()

        self.buttons = []
        self.leftX = 0
        self.leftY = 0
        self.rightX = 0
        self.rightY = 0

    def startTakingInputs(self):

        Thread(target=self.__refresh__, args=()).start()
        return self

    def __refresh__(self):

        while True:
            for e in pygame.event.get():
                if (e.type == pygame.JOYBUTTONDOWN and e.button not in self.buttons):
                    self.buttons.append(e.button)
                if (e.type == pygame.JOYBUTTONUP and e.button in self.buttons):
                    self.buttons.remove(e.button)
                if (e.type == pygame.JOYAXISMOTION):
                    if (e.axis == 0):
                        self.leftX = e.value
                    elif (e.axis == 1):
                        self.leftY = e.value
                    elif (e.axis == 2):
                        self.rightX = e.value
                    elif (e.axis == 3):
                        self.rightY = e.value

    def readLeftValues(self):
        return self.leftX, self.leftY

    def readRightValues(self):
        return self.rightX, self.rightY

    def readButtons(self):
        return self.buttons

    def readValues(self):
        return self.readLeftValues(), self.readRightValues(), self.readButtons()
