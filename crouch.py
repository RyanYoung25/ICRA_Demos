#!/usr/bin/env python

from Maestor import maestor
import time

robot = maestor()

def main():
    bendDown()
    time.sleep(3)
    standUp()


###Using meta-joints,
### Meta-joints are MAESTOR's way of doing inverse kinematics. They work for the legs and allow you to specify the Foot X, Y, and Z. Give them a shot in simulation

def bendDown():
    robot.setProperties("RFZ LFZ", "position position", "-.54 -.54") 
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def standUp():
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")


if __name__ == '__main__':
    main()
