import RPi.GPIO as GPIO
import time

dataPin = 18
sendOutPin = 23
clockPin = 24
resetPin = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(sendOutPin, GPIO.OUT)
GPIO.setup(resetPin, GPIO.OUT)

numbers = [
    [0, 1, 0, 0, 0, 1, 0, 0],  # 0
    [1, 1, 1, 1, 0, 1, 0, 1],  # 1
    [1, 0, 0, 0, 1, 1, 0, 0],  # 2
    [1, 0, 1, 0, 0, 1, 0, 0],  # 3
    [0, 0, 1, 1, 0, 1, 0, 1],  # 4
    [0, 0, 1, 0, 0, 1, 1, 0],  # 5
    [0, 0, 0, 0, 0, 1, 1, 0],  # 6
    [1, 1, 1, 1, 0, 1, 0, 0],  # 7
    [0, 0, 0, 0, 0, 1, 0, 0],  # 8
    [0, 0, 1, 0, 0, 1, 0, 0],  # 9
    [1, 1, 1, 1, 1, 0, 1, 1],  # .
]


def set_pin_value(pin_number, value):
    GPIO.output(pin_number, value)
    time.sleep(0.01)


def add_data_to_register(value):
    set_pin_value(dataPin, value)
    set_pin_value(clockPin, GPIO.HIGH)
    set_pin_value(clockPin, GPIO.LOW)
    set_pin_value(dataPin, GPIO.LOW)


def send_data_out():
    set_pin_value(sendOutPin, GPIO.HIGH)
    set_pin_value(sendOutPin, GPIO.LOW)


def send_number(number):
    data = numbers[number]
    for x in data:
        add_data_to_register(x)
    send_data_out()


def clear_any_number():
    set_pin_value(resetPin, GPIO.LOW)
    set_pin_value(resetPin, GPIO.HIGH)
    data = [1, 1, 1, 1, 1, 1, 1, 1]
    for x in data:
        add_data_to_register(x)
    send_data_out()


def start():
    print('\n-----------------------------------------------------------------')
    print('Insert the number between 0 and 9 that you would like to display:')
    digit = input()
    print('Displaying number: ', digit)
    vector = numbers[digit]
    print('Using vector:', vector)
    send_number(digit)
    start()


clear_any_number()
start()
