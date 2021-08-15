import sys
import RPi.GPIO as GPIO

from devices.servo_finger import ServoFinger

SERVO_PINS = {
    "--increase-temp": 7,
    "--decrease-temp": 13,
    "--change-mode": 15,
}

def print_usage():
    print("USAGE: python retrostat.py <option>.")
    print("\nValid options:"+"".join(['\n  ' + key for key in SERVO_PINS]))
    sys.exit(-1)

if __name__ == "__main__":
    GPIO.setwarnings(False)
    
    if len(sys.argv) < 2:
        print_usage()
        
    command = sys.argv[1]

    if command == "--test":
        for pin in SERVO_PINS.values():
            servo = ServoFinger(pin)
            servo.press_button()
        
    elif command in SERVO_PINS:
        servo = ServoFinger(SERVO_PINS[command])
        servo.press_button()
    
    else:
        print_usage()
