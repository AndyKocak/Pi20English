import RPi.GPIO as GPIO
from time import sleep, time
from threading import Thread


class UltrasonicSensor:

    def __init__(self, echo, trig, setup=GPIO.BOARD):
        self.echo = echo
        self.trig = trig

        self.Time = 0

        self.currentValue = 0

        GPIO.setmode(setup)

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.output(trig, False)

    def startMeasuringDistance(self):

        Thread(target=self.__measureDistance__).start()
        sleep(0.2)

    def readDistance(self):
        return self.currentValue

    def __measureDistance__(self):

        while True:
            GPIO.output(self.trig, True)
            sleep(0.0001)
            GPIO.output(self.trig, False)

            signalBeginning = time()

            while GPIO.input(self.echo) == 1:
                signalEnd = time()

                self.Time = signalEnd - signalBeginning
                self.currentValue = self.Time * 17150
