import PicoAutonomousRobotics
import time
import random
robot = PicoAutonomousRobotics.KitronikPicoRobotBuggy()

notes = {'c':261, 'd':294, 'e':330, 'f':349, 'g':392, 'a':440, 'b':494}
COLOURS = ("BLACK", "RED", "YELLOW", "GREEN", "CYAN", "BLUE", "PURPLE", "WHITE")
LEDs = (0, 1, 2, 3)


ode_to_joy = "e e f g g f e d c c d e e e d d d e e f g g f e d c c d e d d c c"


for note in ode_to_joy.split():
    LED = random.choice(LEDs)
    #print(LED)
    
    colour = random.choice(COLOURS)
    
    robot.soundFrequency(notes[note])
    robot.setLED(LED, robot.RED)
    robot.show()
    time.sleep(0.5)
    robot.silence()
    robot.clear(0)

 
    