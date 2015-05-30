#!/usr/bin/env python

from Maestor import maestor

robot = maestor()

def main():
    setVelocities()
    bendDown()
    waveArms()
    standUp()
    resetVelocities()

def setVelocities():
    robot.setProperties("RSP RSR RSY REP LSP LSR LSY LEP NKY", "velocity velocity velocity velocity velocity velocity velocity velocity velocity", "1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5")

def resetVelocities():
    robot.setProperties("RSP RSR RSY REP LSP LSR LSY LEP NKY", "velocity velocity velocity velocity velocity velocity velocity velocity velocity", "1 1 1 1 1 1 1 1 1")

def waveArms():
    #Raise arms up
    robot.setProperties("RSR LSR RSY LSY", "position position position position", "-1.85 1.85 -1.7 1.7")
    robot.waitForJoint("RSR")
    robot.waitForJoint("LSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("LSY")
    #Loop through waving elbows
    for i in range(0, 3):
        robot.setProperties("REP LEP", "position position", "-1 -1")
        robot.waitForJoint("REP")
        robot.waitForJoint("LEP")
        robot.setProperties("REP LEP", "position position", "0 0")
        robot.waitForJoint("REP")
        robot.waitForJoint("LEP")
    #Lower arms
    robot.setProperties("RSR LSR RSY LSY", "position position position position", "0 0 0 0")
    robot.waitForJoint("RSR")
    robot.waitForJoint("LSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("LSY")

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
