import PicoAutonomousRobotics
import time
import random
robot = PicoAutonomousRobotics.KitronikPicoRobotBuggy()

notes = {'c':261, 'd':294, 'e':330, 'f':349, 'g':392, 'a':440, 'b':494,
         'c2':523, 'd2':587, 'e2':659, 'f2':698, 'g2':784}

robot.soundFrequency(notes['f']) 
time.sleep(0.1)
robot.silence()

robot.soundFrequency(notes['g']) 
time.sleep(0.1)
robot.silence()

robot.soundFrequency(notes['a'])
time.sleep(0.1)
robot.silence()

robot.soundFrequency(notes['c2']) 
time.sleep(0.2)
robot.silence()

robot.soundFrequency(notes['a']) 
time.sleep(0.1)
robot.silence()

robot.soundFrequency(notes['c2']) 
time.sleep(0.5)
robot.silence()