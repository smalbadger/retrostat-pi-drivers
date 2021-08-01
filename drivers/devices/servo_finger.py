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
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPin, GPIO.OUT)
        self.motor = GPIO.PWM(servoPin, 50)

    def press_button(self):
        self.motor.start(7.5)  # 7.5% duty cycle puts motor at 90%
        time.sleep(0.5)
        self.motor.ChangeDutyCycle(0)