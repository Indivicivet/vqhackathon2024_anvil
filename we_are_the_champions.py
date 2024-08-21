import PicoAutonomousRobotics
import time
import random
robot = PicoAutonomousRobotics.KitronikPicoRobotBuggy()

notes = {'c':261, 'd':294, 'e':330, 'f':349, 'g':392, 'a':440, 'b':494,
         'c2':523, 'd2':587, 'e2':659, 'f2':698, 'g2':784}
COLOURS = ("BLACK", "RED", "YELLOW", "GREEN", "CYAN", "BLUE", "PURPLE", "WHITE")
LEDs = (0, 1, 2, 3)

robot.soundFrequency(notes['c2']) #we
time.sleep(2)
robot.silence()

robot.soundFrequency(notes['b']) #are
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['c2']) #the
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['b']) #cham
time.sleep(1)
robot.silence()

robot.soundFrequency(notes['g']) #pions
time.sleep(1.5)
robot.silence()

robot.soundFrequency(notes['e']) #my
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['a']) #fri
time.sleep(1)
robot.silence()

robot.soundFrequency(notes['e']) #end
time.sleep(1.5)
robot.silence()

time.sleep(1)

robot.soundFrequency(notes['g']) #and
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['c2']) #we'll
time.sleep(2)
robot.silence()

robot.soundFrequency(notes['d2']) #keep
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['e2']) #on
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['g2']) #fight
time.sleep(1)
robot.silence()

robot.soundFrequency(notes['e2']) #ing
time.sleep(1)
robot.silence()

robot.soundFrequency(notes['a']) #till
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['b']) #the
time.sleep(0.5)
robot.silence()

robot.soundFrequency(notes['a']) #end
time.sleep(3)
robot.silence()