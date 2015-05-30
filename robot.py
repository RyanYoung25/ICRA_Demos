#!/usr/bin/env python

from Maestor import maestor

robot = maestor()

def main():
    setVelocities()
    bendDown()
    doTheRobot()
    standUp()
    resetVelocities()

def setVelocities():
    robot.setProperties("RSP RSR RSY REP NKY", "velocity velocity velocity velocity velocity", "1.5 1.5 1.5 1.5 1.5")

def resetVelocities():
    robot.setProperties("RSP RSR RSY REP NKY", "velocity velocity velocity velocity velocity", "1 1 1 1 1")

def bendDown():
    robot.setProperties("RFZ LFZ", "position position", "-.54 -.54")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def standUp():
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def doTheRobot():
    robot.setProperties("RSY RSR", "position position", "1.57 -1.35")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.setProperty("REP", "velocity", 2)
    for i in range(0, 2):
        robot.setProperty("REP", "position", -1.7)
        robot.waitForJoint("REP")
        robot.setProperty("REP", "position", 0)
        robot.waitForJoint("REP")
    robot.setProperties("RSY RSR NKY", "position position position", "0 0 0")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")



if __name__ == '__main__':
    main()
