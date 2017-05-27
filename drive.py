import RPi.GPIO as GPIO

PWM_FREQ = 50
CENTER_DUTY = 0.075
MAX_DUTY = 0.025
SPEED_PWM = 5
TURN_PWM = 3

class Driver(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SPEED_PWM, GPIO.OUT)
        GPIO.setup(TURN_PWM, GPIO.OUT)

        self.speed_pwm = GPIO.PWM(SPEED_PWM, PWM_FREQ)
        self.turn_pwm = GPIO.PWM(TURN_PWM, PWM_FREQ)

        self.speed_pwm.start(0)
        self.turn_pwm.start(0)
        
    def set_state(self, speed, turn):
        self.speed_pwm.ChangeDutyCycle(CENTER_DUTY + MAX_DUTY * speed)
        self.turn_pwm.ChangeDutyCycle(CENTER_DUTY + MAX_DUTY * turn)

    def kill(self):
        self.speed_pwm.stop()
        self.turn_pwm.stop()
        GPIO.cleanup()
