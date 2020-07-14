from pololu_drv8835_rpi import motors
import math


class MotorControl:

    def __init__(self):
        self.rightSpeed = 0
        self.leftSpeed = 0

    def adjustSpeed(self, hizSag, hizSol):
        self.rightSpeed = rightSpeed
        self.leftSpeed = leftSpeed

        480 if rightSpeed > 480 else rightSpeed
        -480 if rightSpeed < -480 else rightSpeed

        480 if leftSpeed > 480 else leftSpeed
        -480 if leftSpeed < -480 else leftSpeed

        motors.setSpeeds(rightSpeed, leftSpeed)

    def changeControllerValueToMotorValue(self, x, y):
        r = math.hypot(x, y)
        t = math.atan2(y, x)

        # rotate by 45 degrees
        t += math.pi / 4

        # back to cartesian
        left = r * math.cos(t)
        right = r * math.sin(t)

        # rescale the new coords
        left = left * math.sqrt(2)
        right = right * math.sqrt(2)

        # clamp to -1/+1
        left = max(-1, min(left, 1))
        right = max(-1, min(right, 1))

        return int(left * 480), -int(right * 480)
