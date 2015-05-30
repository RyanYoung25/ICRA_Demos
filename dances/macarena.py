#!/usr/bin/env python
#to run a script: type in console <initRobot("")> <Enter>
#also in console <command("EnableAll", "")> <Enter>



from Maestor import maestor
import sys

def armsout(robot):
    #arms moved from hubo's side/ original position to flat in front of hubo. palms are down
    #right arm move
    robot.setProperty("RSP", "position", -1.4)
    robot.setProperty("RWY", "position", -1.6)
    robot.setProperty("REP", "position", 0.00)
    robot.setProperty("RWY", "position", 1.60)
    #right arm wait
    robot.waitForJoint("RSP")
    robot.waitForJoint("RWY")
    robot.waitForJoint("REP")
    robot.waitForJoint("RWY")
    #left arm move
    robot.setProperty("LSP", "position", -1.4)
    robot.setProperty("LWY", "position", 1.6)
    robot.setProperty("LEP", "position", 0.00)
    robot.setProperty("LWY", "position", -1.60)
    #left arm wait
    robot.waitForJoint("LSP")
    robot.waitForJoint("LWY")
    robot.waitForJoint("LEP")
    robot.waitForJoint("LWY")
    
def handflip(robot):
    #flip both hands, should be palm down first.
    #right, then left
    robot.setProperty("RWY", "position", -1.5)
    robot.setProperty("RWY", "speed", 2)
    robot.waitForJoint("RWY")

    robot.setProperty("LWY", "position", 1.50)
    robot.setProperty("LWY", "speed", 2)
    robot.waitForJoint("LWY")

def handhead(robot):
    # moves the hands from in front of him to on either side of his head. first right, then a wait, then left, then wait
    robot.setProperty("RSP", "position", -2.5)
    robot.setProperty("RSR", "position", -0.66)
    robot.setProperty("RSY", "position", 1.25)
    robot.setProperty("REP", "position", -1.75)
    #robot.setProperty("RSP", "position", )
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")
    #robot.waitForJoint("R")
    robot.setProperty("LSP", "position", -2.5)
    robot.setProperty("LSR", "position", 0.66)
    robot.setProperty("LSY", "position", -1.25)
    robot.setProperty("LEP", "position", -1.75)
    #robot.setProperty("RSP", "position", )
    robot.waitForJoint("LSP")
    robot.waitForJoint("LSR")
    robot.waitForJoint("LSY")
    robot.waitForJoint("LEP")
    #robot.waitForJoint("R")

def handhips(robot):
    #right upper body: moves his right harm from his head to hips
    robot.setProperty("RSP", "position", 0.01)
    robot.setProperty("RSR", "position", -0.75)
    robot.setProperty("RSY", "position", 1.25)
    robot.setProperty("REP", "position", -1.40)
    robot.setProperty("RWY", "position", -1.60)
    robot.setProperty("RWP", "position", 0.01)
    #right wait info: gives all of the arm time to move
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")
    robot.waitForJoint("RWY")
    robot.waitForJoint("RWP")
    #left upper body: moves his left arm from his head to hips
    robot.setProperty("LSP", "position", 0.01)
    robot.setProperty("LSR", "position", 0.75)
    robot.setProperty("LSY", "position", -1.25)
    robot.setProperty("LEP", "position", -1.40)
    robot.setProperty("LWY", "position", 1.60)
    robot.setProperty("LWP", "position", 0.01)
    #left wait stuff: gives the arm time to move
    robot.waitForJoint("LSP")
    robot.waitForJoint("LSR")
    robot.waitForJoint("LSY")
    robot.waitForJoint("LEP")
    robot.waitForJoint("LWY")
    robot.waitForJoint("LWP")


def twerkin(robot): #the closest hubo gets to twerking. His hands should still be on his sides
    for x in xrange(0,2 ):
        robot.setProperty("WST", "position", -.65)
        robot.waitForJoint("WST")
        robot.setProperty("WST", "position", .65)
        robot.waitForJoint("WST")
        robot.command("Zero", "WST")


def clear(robot): #resets all positions afterwards
    robot.command("ZeroAll", "")

def backToHome(robot):
    #right side position
    robot.setProperty("RSP", "position", 0)
    robot.setProperty("RSR", "position", 0)
    robot.setProperty("RSY", "position", 0)
    robot.setProperty("REP", "position", 0)
    robot.setProperty("RWY", "position", 0)
    robot.setProperty("RWP", "position", 0)
    #left side position
    robot.setProperty("LSP", "position", 0)
    robot.setProperty("LSR", "position", 0)
    robot.setProperty("LSY", "position", 0)
    robot.setProperty("LEP", "position", 0)
    robot.setProperty("LWY", "position", 0)
    robot.setProperty("LWP", "position", 0)

def main(): #combines everything, this is the aggregatee
    robot = maestor()
    armsout(robot)
    handflip(robot)
    handhead(robot)
    handhips(robot)
    twerkin(robot)
    clear(robot)



if __name__ == "__main__":
    main()


