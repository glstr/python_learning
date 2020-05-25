#!/usr/bin/python
# coding:utf-8
import RPi.GPIO as GPIO
import sys 
import time

# led color 
RED = 1
GREEN = 2
BLUE = 3

# engine direction
BRAKE = 0 
FORWARD = 1
BACK = 2
LEFT = 3
RIGHT = 4
SPIN_LEFT = 5
SPIN_RIGHT = 6


class LED:
    def __init__(self):
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24
        
    def load(self):
        GPIO.setup(self.LED_R, GPIO.OUT)
        GPIO.setup(self.LED_G, GPIO.OUT)
        GPIO.setup(self.LED_B, GPIO.OUT)

    def release(self):
        pass

    def set_color(self, color):
        if color == RED:
            GPIO.output(self.LED_R, GPIO.HIGH)
            GPIO.output(self.LED_G, GPIO.LOW)
            GPIO.output(self.LED_B, GPIO.LOW)
        elif color == GREEN:
            GPIO.output(self.LED_R, GPIO.LOW)
            GPIO.output(self.LED_G, GPIO.HIGH)
            GPIO.output(self.LED_B, GPIO.LOW)
        elif color == BLUE:
            GPIO.output(self.LED_R, GPIO.LOW)
            GPIO.output(self.LED_G, GPIO.LOW)
            GPIO.output(self.LED_B, GPIO.HIGH)
        else:
            print "not support"
        return 

class Sensor:
    def __init__(self):
        self.AvoidSensorLeft = 12
        self.AvoidSensorRight = 17

    def load(self):
        GPIO.setup(self.AvoidSensorLeft,GPIO.IN)
        GPIO.setup(self.AvoidSensorRight,GPIO.IN)


class Engine:
    def __init__(self):
        self.IN1 = 20
        self.IN2 = 21
        self.IN3 = 19
        self.IN4 = 26
        self.ENA = 16
        self.ENB = 13

        self.pwm_ENA = None
        self.pwm_ENB = None
        
        self.delaytime = 2

    def load(self):
        GPIO.setup(self.ENA,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(self.IN1,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN2,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.ENB,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(self.IN3,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN4,GPIO.OUT,initial=GPIO.LOW)
        #设置pwm引脚和频率为2000hz
        self.pwm_ENA = GPIO.PWM(self.ENA, 2000)
        self.pwm_ENB = GPIO.PWM(self.ENB, 2000)
        self.pwm_ENA.start(0)
        self.pwm_ENB.start(0)

    def release(self):
        self.pwm_ENA.stop()
        self.pwm_ENB.stop()

    def brake(self, delaytime):
        print "stop"
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)

    def run(self, delaytime):
        print "forward"
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        #启动PWM设置占空比为100（0--100）
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        #self.pwm_ENA.start(100)
        #self.pwm_ENB.start(100)
        time.sleep(delaytime)
        self.brake(delaytime)

    def back(self, delaytime):
        print "back"
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)
        self.brake(delaytime)

    def left(self, delaytime):
        print "left"
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)
        self.brake(delaytime)

    def right(self, delaytime):
        print "right"
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)
        self.brake(delaytime)

    def spin_left(self, delaytime):
        print "spin_left"
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)

    def spin_right(self, delaytime):
        print "spin_right"
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_ENA.ChangeDutyCycle(80)
        self.pwm_ENB.ChangeDutyCycle(80)
        time.sleep(delaytime)


class SmartCar:
    def __init__(self):
        self.led = LED()
        self.engine = Engine()
        self.status = 0

    def load(self):
        self._gpio_load()        

        self.led.load()
        self.engine.load()

        self.status = 1

    def _gpio_load(self):
        #init GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def release(self):
        self.engine.release()
        self.led.release()

        self._gpio_release()

        self.status = 0 

    def _gpio_release(self):
        GPIO.cleanup()

    def set_led_color(self, color):
        self.led.set_color(color)

    def run(self, direction, delaytime):
        if direction == BRAKE:
            self.engine.brake(delaytime)
        elif direction == FORWARD:
            self.engine.run(delaytime)
        elif direction == BACK:
            self.engine.back(delaytime)
        elif direction == LEFT:
            self.engine.left(delaytime)
        elif direction == RIGHT:
            self.engine.right(delaytime)
        elif direction == SPIN_LEFT:
            self.engine.spin_left(delaytime) 
        elif direction == SPIN_RIGHT:
            self.engine.spin_right(delaytime)
        else:
            pass 

    def info(self):
        return self.status  

    
def usage():
    print "usage:"
    print "python *.py method param"
    print "support method:"
    print "check"
    return 


def check(params):
    car = SmartCar()
    car.load()
    print car.info()
    car.set_led_color(BLUE)
    try:
        car.run(FORWARD, 1)
        car.run(BACK, 1)
    except Exception as e:
        print e
    time.sleep(10)
    car.release()

methods = {"check": check}

def cmd(method, param):
    if method in methods:
        methods[method](param)
    else:
        print "no support method"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)

    method = sys.argv[1]
    params = ""
    if len(sys.argv) > 2:
        params = sys.argv[2]
    
    cmd(method, params) 

