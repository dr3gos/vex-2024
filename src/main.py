
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Project:      AISB VEX 23'-24' Test Code                                   #
# 	Author:       Dragos S.                                                    #
# 	Created:      26/09/2023                                                   #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

controller_1 = Controller(PRIMARY)
leftRear = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)       
rightRear = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)       
leftFront = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)       
rightFront = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
throwMotor = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)

leftLifter = Motor (Ports.PORT1, GearSetting.RATIO_18_1, False)
rightLifter = Motor (Ports.PORT2, GearSetting.RATIO_18_1, True)
leftLifter.set_stopping(HOLD)
rightLifter.set_stopping(HOLD)

wait(30, MSEC)

# Functions

def move(direction, power, duration):
# 1 = forward, 2 = backward, 3 = left, 4 = right
    if direction == 1:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(REVERSE)
        leftRear.spin(REVERSE)
        rightRear.spin(REVERSE)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 2:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD)
        rightFront.spin(FORWARD)
        leftRear.spin(FORWARD)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 3:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD) #f
        rightFront.spin(REVERSE) #r
        leftRear.spin(FORWARD) #f
        rightRear.spin(REVERSE) #r
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 4:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(FORWARD)
        leftRear.spin(REVERSE)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 5:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD)
        rightFront.spin(REVERSE)
        leftRear.spin(REVERSE)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 6:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(FORWARD)
        leftRear.spin(FORWARD)
        rightRear.spin(REVERSE)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()

def lifing():
    if controller_1.buttonL2.pressing():
        power = 100
    elif controller_1.buttonR2.pressing():
        power = -100
    else:
        power = 0
    leftLifter.set_velocity(power, PERCENT)
    rightLifter.set_velocity(power, PERCENT)
    leftLifter.spin(FORWARD)
    rightLifter.spin(FORWARD)

def tuck():
    throwMotor.set_velocity(100, PERCENT)
    throwMotor.spin(FORWARD)
    wait(300, MSEC)
    throwMotor.stop()

def untuck():
    throwMotor.set_velocity(100, PERCENT)
    throwMotor.spin(REVERSE)
    wait(300, MSEC)
    throwMotor.stop()

def throwFar():
    power = 70
    throwMotor.set_velocity(100, PERCENT)
    

    leftFront.set_velocity(power, PERCENT)
    rightFront.set_velocity(power, PERCENT)
    leftRear.set_velocity(power, PERCENT)
    rightRear.set_velocity(power, PERCENT)

    leftFront.spin(REVERSE)
    rightFront.spin(REVERSE)
    leftRear.spin(REVERSE)
    rightRear.spin(REVERSE)

    wait(250, MSEC)
    throwMotor.spin(FORWARD)
    wait(200, MSEC)

    leftFront.stop()
    rightFront.stop()
    leftRear.stop()
    rightRear.stop()
    throwMotor.stop()

    wait(100, MSEC)
    throwMotor.set_velocity(100, PERCENT)
    throwMotor.spin(REVERSE)
    wait(60, MSEC)
    throwMotor.stop()
    untuck()

def autonmousleft():
    # move(3, 20, 1000)
    # throwFar()
    # wait(500, MSEC)
    move(1, 40, 2500)
    tuck()
    move(2, 40, 3000)
    # move(4, 40, 1000)
    move(6, 40, 3500)

def autonmousright():
    # move(4, 20, 1000)
    # throwFar()
    # wait(500, MSEC)
    move(1, 40, 2500)
    # tuck()
    # move(2, 40, 4500)
    # move(5, 40, 2500)



def driving():
    turn = -controller_1.axis1.position() #updown left
    speed = -controller_1.axis3.position() #leftright left
    strafe = -controller_1.axis4.position() #lefright right

    leftFrontPower = speed + turn + strafe;
    rightFrontPower = speed - turn - strafe;
    leftRearPower = speed + turn - strafe;
    rightRearPower = speed - turn + strafe;

    leftFront.set_velocity(leftFrontPower, PERCENT)
    rightFront.set_velocity(rightFrontPower, PERCENT)
    leftRear.set_velocity(leftRearPower, PERCENT)
    rightRear.set_velocity(rightRearPower, PERCENT)

    leftFront.spin(FORWARD)
    rightFront.spin(FORWARD)
    leftRear.spin(FORWARD)
    rightRear.spin(FORWARD)

def throw():
    if controller_1.buttonR1.pressing():
        tPower = 100
    elif controller_1.buttonL1.pressing():
        tPower = -100
    else:
        tPower = 0
    # tPow er = controller_1.axis2.position()
    throwMotor.set_velocity(tPower, PERCENT)
    throwMotor.spin(FORWARD)



# init code
retarder = 1
lrretarder = 1


# Main loop
while 1:
    if controller_1.buttonRight.pressing():
        autonmousright()
    
    if controller_1.buttonLeft.pressing():
        autonmousleft()

    if controller_1.buttonUp.pressing():
        while 1:
            driving()
            throw()
            lifing()
            if controller_1.buttonA.pressing():
                throwFar()
            if controller_1.buttonUp.pressing():
                if retarder < 1:
                    retarder = round(retarder + 0.1, 2)
                    controller_1.rumble("-")
                    # retarderString = "Retarder: " + str(round(retarder, 2))
                    retarderString = "Retarder: " + str(retarder )
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(retarderString)
                wait(100, MSEC)
            if controller_1.buttonDown.pressing():
                if retarder >= 0.1:
                    retarder = round(retarder - 0.1, 2)
                    controller_1.rumble("-")
                    retarderString = "Retarder: " + str(round(retarder, 2))
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(retarderString)
            if controller_1.buttonLeft.pressing():
                if lrretarder < 1:
                    lrretarder = round(lrretarder + 0.1, 2)
                    lrretarderString = "LR Retarder: " + str(round(lrretarder, 2))
                    controller_1.rumble("-")
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(lrretarderString)
                wait(100, MSEC)
            if controller_1.buttonRight.pressing():
                if lrretarder >= 0.1:
                    lrretarder = round(lrretarder - 0.1, 2)
                    lrretarderString = "LR Retarder: " + str(round(lrretarder, 2))
                    controller_1.rumble("-")
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(lrretarderString)
                    wait(100, MSEC)

wait(5, MSEC)