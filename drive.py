import RPi.GPIO as GPIO

#import pigpio

PWM_FREQ = 50
CENTER_DUTY = 7.5
MAX_DUTY = 0.025
SPEED_PWM = 11
TURN_PWM = 7

#SPEED_GPIO = 2
#TURN_GPIO = 3

class Driver(object):
    def __init__(self):
        #self.pi = pigpio.pi()
        #self.pi.set_mode(SPEED_GPIO, pigpio.OUTPUT)
        #self.pi.set_mode(TURN_GPIO, pigpio.OUTPUT)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SPEED_PWM, GPIO.OUT)
        GPIO.setup(TURN_PWM, GPIO.OUT)

        self.speed_pwm = GPIO.PWM(SPEED_PWM, PWM_FREQ)
        self.turn_pwm = GPIO.PWM(TURN_PWM, PWM_FREQ)

        self.speed_pwm.start(0)
        self.turn_pwm.start(0)

        
    def set_state(self, speed, turn):
        duty_speed = CENTER_DUTY + MAX_DUTY * speed
        duty_turn = CENTER_DUTY + MAX_DUTY * (- turn - 21)
        duty_turn = max(4.8, min(9.0, duty_turn))
        #print(duty_turn)
        self.speed_pwm.ChangeDutyCycle(duty_speed)
        self.turn_pwm.ChangeDutyCycle(duty_turn)

        #duty_speed = 1500 + 5 * speed
        #duty_turn = 1500 + 5 * turn

        #self.pi.set_servo_pulsewidth(SPEED_GPIO, duty_speed)
        #self.pi.set_servo_pulsewidth(TURN_GPIO, duty_turn)

        #print("speed: " + str(duty_speed/100.0 / PWM_FREQ * 1000.0) + " ms high")
        #print("turn: " + str(duty_turn/100.0 / PWM_FREQ * 1000.0) + " ms high")
        #print("speed: " + str(duty_speed) + " high")
        #print("turn: " + str(duty_turn) + " high")

    def kill(self):
        self.speed_pwm.stop()
        self.turn_pwm.stop()
        GPIO.cleanup()
