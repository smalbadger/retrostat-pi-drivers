import sys

SERVO_PINS = {
    "--increase-temp": 0,
    "--decrease-temp": 1,
    "--change-mode": 2,
}

if __name__ == "__main__":
    command = sys.argv[1]

    if command in SERVO_PINS:
        from lib.servo_finger import ServoFinger
        servo = ServoFinger(SERVO_PINS[command])
        servo.press_button()
    else:
        print("USAGE: python retrostat.py <option>.")
        print("\nValid options:"+"".join(['\n  ' + key for key in SERVO_PINS]))