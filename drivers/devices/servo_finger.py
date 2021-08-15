"""
Author:         Sam Badger
Date Created:   July 22, 2021
Description:    Simple servo controller for pressing buttons
credits to https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/ for showing how to use a servo motor
"""
import RPi.GPIO as GPIO
import time

class ServoFinger():

    def __init__(self, servoPin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servoPin, GPIO.OUT)
        self.motor = GPIO.PWM(servoPin, 50)
        self.motor.start(10)
        time.sleep(0.5)

    def press_button(self):
        self.motor.ChangeDutyCycle(5)
        time.sleep(0.5)
        self.motor.ChangeDutyCycle(10)
