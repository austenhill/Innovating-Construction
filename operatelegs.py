# Operate Legs will be called with an argument. Options are: -e --extend ; -c --close
# operatelegs.py --extend or operatelegs.py -e
# operatelegs.py --close or operatelegs.py -c
# C for close also means to retract

# Initialize
import RPi.GPIO as GPIO
import sys, getopt
import time
GPIO.setmode (GPIO.BOARD)

# Argument list with long and short options
argumentList = sys.argv[1:]
options = "ec:"
long_options = ["extend", "close"]

# Leg-pin assignments:
legPins = {
    'backLeftExtend': 29,    # GPIO 5
    'backLeftRetract': 31,   # GPIO 6
    'backRightExtend': 36,   # GPIO 16
    'backRightRetract': 11,  # GPIO 17
    'frontLeftExtend': 15,   # GPIO 22
    'frontLeftRetract': 16,  # GPIO 23
    'frontRightExtend': 18,  # GPIO 24
    'frontRightRetract': 22  # GPIO 25
}

# Initialize each GPIO port
for assignment in legPins:
    pin = legPins[assignment]
    GPIO.setup(pin, GPIO.OUT)

# Extend legs function
def extend():
    GPIO.output(legPins['backLeftExtend'], GPIO.LOW)
    GPIO.output(legPins['backRightExtend'], GPIO.LOW)
    GPIO.output(legPins['frontLeftExtend'], GPIO.LOW)
    GPIO.output(legPins['frontRightExtend'], GPIO.LOW)
    time.sleep (10)
    GPIO.cleanup()
    return

# Retract legs function
def retract():
    GPIO.output(legPins['backLeftRetract'], GPIO.LOW)
    GPIO.output(legPins['backRightRetract'], GPIO.LOW)
    GPIO.output(legPins['frontLeftRetract'], GPIO.LOW)
    GPIO.output(legPins['frontRightRetract'], GPIO.LOW)
    time.sleep (10)
    GPIO.cleanup()
    return

# Parse the argument and call the appropriate function to operate the legs
# For close operation just use --close for the argument
try:

	arguments, values = getopt.getopt(argumentList, options, long_options)
	
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-e", "--extend"):
			extend()
			
		elif currentArgument in ("-c", "--close"):
			retract()
			
except getopt.error as err:
	print (str(err))
