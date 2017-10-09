import time

class Motor
    def __init__(self, io, input1, input2, enable):
        self.input1 = input1
        self.input2 = input2
        self.enable = enable

class Car
    def __init__(self, io):
        self.speed = 100

        self.io = io

        self.Motor1_input1 = 2
        self.Motor1_input2 = 4
        self.Motor1_enable = 17

        self.Motor2_input1 = 11
        self.Motor2_input2 = 10
        self.Motor2_enable = 22

        io.setup(self.Motor1_input1, io.OUT)
        io.setup(self.Motor1_input2, io.OUT)
        io.setup(self.Motor1_enable, io.OUT)

        self.right_wheel = io.PWM(self.Motor1_enable, 150)
        self.right_wheel.start(0)
        self.right_wheel.ChangeDutyCycle(0)

        io.setup(self.Motor2_input1, io.OUT)
        io.setup(self.Motor2_input2, io.OUT)
        io.setup(self.Motor2_enable, io.OUT)

        self.left_wheel = io.PWM(self.Motor2_enable, 150)
        self.left_wheel.start(0)
        self.left_wheel.ChangeDutyCycle(0)

    # Shutoff all the motors
    def shutoff(self, io):
        io.output(self.Motor1_input1, False)
        io.output(self.Motor1_input2, False)
        io.output(self.Motor1_enable, False)

        io.output(self.Motor2_input1, False)
        io.output(self.Motor2_input2, False)
        io.output(self.Motor2_enable, False)

    # Motor1 foward
    def motor1_forward(self):
        self.io.output(self.Motor1_input1, True)
        self.io.output(self.Motor1_input2, False)
        self.io.output(self.Motor1_enable, True)

    # Motor2 forward
    def motor2_forward(self):
        self.io.output(self.Motor2_input1, False)
        self.io.output(self.Motor2_input2, True)
        self.io.output(self.Motor2_enable, True)

    # Motor1 reverse
    def motor1_reverse(self):
        io.output(self.Motor1_input1, False)
        io.output(self.Motor1_input2, True)
        io.output(self.Motor1_enable, True)

    # Motor2 reverse
    def motor2_reverse(self):
        io.output(self.Motor2_input1, True)
        io.output(self.Motor2_input2, False)
        io.output(self.Motor2_enable, True)

    def car_forward(self, tw = 0):
        self.motor1_forward()
        self.motor2_forward()
        self.right_wheel.ChangeDutyCycle(self.speed-2)
        self.left_wheel.ChangeDutyCycle(self.speed)
        if tw != 0:
            time.sleep(tw)

    def car_reverse(self, tw = 0):
        self.motor1_reverse()
        self.motor2_reverse()
        self.right_wheel.ChangeDutyCycle(self.speed - 2)
        self.left_wheel.ChangeDutyCycle(self.speed)
        if tw != 0:
            time.sleep(tw)

    def car_left(self, tw = 0):
        self.motor1_forward()
        self.motor2_forward()
        rw.ChangeDutyCycle(self.speed)
        lw.ChangeDutyCycle(speed - speed * 0.4)
        if tw != 0:
            time.sleep(tw)

    def car_right(self, tw = 0):
        self.motor1_forward()
        self.motor2_forward()
        self.right_wheel.ChangeDutyCycle(self.speed - self.speed * 0.4)
        self.left_wheel.ChangeDutyCycle(self.speed)
        if tw != 0:
            time.sleep(tw)

    def car_rotate_right(self, tw = 0):
        self.motor1_reverse()
        self.motor2_forward()
        self.right_wheel.ChangeDutyCycle(self.speed)
        self.left_wheel.ChangeDutyCycle(self.speed)
        if tw != 0:
            time.sleep(tw)

    def car_rotate_left(self, tw = 0):
        self.motor1_forward()
        self.motor2_reverse()
        self.right_wheel.ChangeDutyCycle(self.speed)
        self.left_wheel.ChangeDutyCycle(self.speed)
        if tw != 0:
            time.sleep(tw)