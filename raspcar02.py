import RPi.GPIO as io
io.setmode(io.BCM) # @TODO: is this the best option to access the pin #s?
import sys, tty, termios, time
io.cleanup()

# Speed definition
speed = 100
print("speed is on 5")

# Right Wheel
Motor1_input1 = 2
Motor1_input2 = 4

Motor1_enable = 17
io.setup(Motor1_input1, io.OUT)
io.setup(Motor1_input2, io.OUT)
io.setup(Motor1_enable, io.OUT)
rw = io.PWM(Motor1_enable,150)
rw.start(0)
rw.ChangeDutyCycle(0)

# Left Wheel
Motor2_input1 = 11
Motor2_input2 =	10

Motor2_enable = 22
io.setup(Motor2_input1, io.OUT)
io.setup(Motor2_input2, io.OUT)
io.setup(Motor2_enable, io.OUT)
lw = io.PWM(Motor2_enable,150)
lw.start(0)
lw.ChangeDutyCycle(0)

# io.setup(9, io.IN) #Sensor Pin

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def allOff():
	io.output(Motor1_input1,False)
	io.output(Motor1_input2,False)
	io.output(Motor1_enable,False)
	io.output(Motor2_input1,False)
	io.output(Motor2_input2,False)
	io.output(Motor2_enable,False)

def motor1_forward():
	io.output(Motor1_input1,True)
	io.output(Motor1_input2,False)
	io.output(Motor1_enable,True)

def motor1_reverse():
	io.output(Motor1_input1,False)
	io.output(Motor1_input2,True)
	io.output(Motor1_enable,True)

def motor2_forward():
	io.output(Motor2_input1,False)
	io.output(Motor2_input2,True)
	io.output(Motor2_enable,True)

def motor2_reverse():
	io.output(Motor2_input1,True)
	io.output(Motor2_input2,False)
	io.output(Motor2_enable,True)

def carForward(tw = 0):
	motor1_forward()
	motor2_forward()
	rw.ChangeDutyCycle(speed-2)
	lw.ChangeDutyCycle(speed)
	if(tw != 0):
		time.sleep(tw)

def carReverse(tw = 0):
	motor1_reverse()
	motor2_reverse()
	rw.ChangeDutyCycle(speed-2)
	lw.ChangeDutyCycle(speed)
	if(tw != 0):
		time.sleep(tw)

def carLeft(tw = 0):
	motor1_forward()
	motor2_forward()
	rw.ChangeDutyCycle(speed)
	lw.ChangeDutyCycle(speed - speed * 0.4)
	if(tw != 0):
		time.sleep(tw)

def carRight(tw = 0):
	motor1_forward()
	motor2_forward()
	rw.ChangeDutyCycle(speed - speed * 0.4)
	lw.ChangeDutyCycle(speed)
	if(tw != 0):
		time.sleep(tw)

def carRotateRight(tw = 0):
	motor1_reverse()
	motor2_forward()
	rw.ChangeDutyCycle(speed)
	lw.ChangeDutyCycle(speed)
	if(tw != 0):
		time.sleep(tw)

def carRotateLeft(tw = 0):
	motor1_forward()
	motor2_reverse()
	rw.ChangeDutyCycle(speed)
	lw.ChangeDutyCycle(speed)
	if(tw != 0):
		time.sleep(tw)


# allOff();
while True:
	char = getch()
	#Speed Control
	if(char == "1"):
		print("Speed 1")
		speed = 50
	if(char == "2"):
		print("Speed 2")
		speed = 60
	if(char == "3"):
		print("Speed 3")
		speed = 70
	if(char == "4"):
		print("Speed 4")
		speed = 80
	if(char == "5"):
		print("Speed 5")
		speed = 90
	if(char == "6"):
		print("Speed 6 - MAX SPEED")
		speed = 100
	if(char == "w"):
		print("Forward")
		carForward()
	if(char == "s"):
		print("Reverse")
		carReverse()
	if(char == "d"):
		print("Turning right")
		carRight()
	if(char == "a"):
		print("Turning left")
		carLeft()
	if(char == "r"):
		print("Rotating left")
		carRotateLeft()
	if(char == "f"):
		print("Rotating right")
		carRotateRight()
	if(char == "q"):
		print("Car stopped")
		allOff();
	if(char == "e"):
		print("Making 8\'s")
		carForward(2)
		carRight(7)
		carForward(2)
		carLeft(5)
		carForward(2)
		allOff();
	# if(char == "t"):
	# 	sensorSteering()
	if(char == "x"):
		print("Program ended")
		break

	char = ""

io.cleanup()
