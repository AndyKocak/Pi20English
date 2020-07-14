from time import sleep
import RPi.GPIO as GPIO
from threading import Thread


class ServoControl:

    def __init__(self, pin, GPIOSetup=GPIO.BOARD):
        GPIO.setmode(GPIOSetup)

        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.pin = pin
        self.targetAngle = 90
        self.currentAngle = 90
        self.sleeping = True
        self.continuous = False

    def setToContinuousSpin(self):
        self.sleeping = True
        GPIO.output(self.pin, True)

    def setToSingleSpin(self):
        self.continuous = False
        GPIO.output(self.pin, False)

    def __setSingleAngle__(self):
        signalLength = self.targetAngle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(signalLength)

        deltaAngle = abs(self.targetAngle - self.currentAngle)
        requiredSleep = deltaAngle / 150
        sleep(requiredSleep)  # experimental value
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.currentAngle = self.targetAngle
        self.sleeping = True

    def __setContinuousAngle__(self, angle):
        duty = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty)

    def setAngle(self, angle):

        self.targetAngle = angle

        if self.continuous:
            self.__setContinuousAngle__(self.targetAngle)
        elif self.sleeping and (self.currentAngle is not self.targetAngle):
            self.sleeping = False


