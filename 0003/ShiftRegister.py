import tkinter as tk
import RPi.GPIO as GPIO
import time

# Initialise variables
root = tk.Tk()
rows, columns = 8, 8
btnMatrix = [[0 for x in range(rows)] for y in range(columns)]

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


def set_pin_value(pin_number, value):
    GPIO.output(pin_number, value)
    time.sleep(0.01)


def reset_shift_register():
    set_pin_value(dataPin, GPIO.LOW)
    set_pin_value(clockPin, GPIO.LOW)
    set_pin_value(resetPin, GPIO.LOW)
    send_data_out()
    set_pin_value(resetPin, GPIO.HIGH)


def add_data_to_register(value):
    set_pin_value(dataPin, value)
    set_pin_value(clockPin, GPIO.HIGH)
    set_pin_value(clockPin, GPIO.LOW)
    set_pin_value(dataPin, GPIO.LOW)


def send_data_out():
    set_pin_value(sendOutPin, GPIO.HIGH)
    set_pin_value(sendOutPin, GPIO.LOW)


def button_grid_click(row_number, column_number):
    btn_text = btnMatrix[row_number][column_number]["text"];
    if btn_text == "0":
        btnMatrix[row_number][columnNumber].config(bg="red", text="1")
    else:
        btnMatrix[row_number][columnNumber].config(bg="lightgray", text="0")


def button_run_click():
    reset_shift_register()
    for x in reversed(btnMatrix[0]):
        if x["text"] == "1":
            add_data_to_register(1)
        else:
            add_data_to_register(0)
    send_data_out()


def close_window():
    reset_shift_register()
    root.destroy()


# Main
root.protocol("WM_DELETE_WINDOW", close_window)
reset_shift_register()

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)
bottom_frame = tk.Frame(root).pack(side="bottom")

for columnNumber in range(8):
    btnMatrix[0][columnNumber] = tk.Button(top_frame, text="0", bg="lightgray",
                                           command=lambda x1=0, y1=columnNumber: button_grid_click(x1, y1), height=1,
                                           width=5)
    btnMatrix[0][columnNumber].grid(row=0, column=columnNumber)

btnSend = tk.Button(bottom_frame, text="Send", bg="darkgreen", fg="white", height=1, width=5,
                    command=button_run_click).pack()

root.mainloop()
