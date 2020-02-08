import tkinter as tk
from . LedMatrix8x8Templates import all_characters
import RPi.GPIO as GPIO

runGrid = False  # Global flag
idx = 0  # loop index
testAll = False  # Global flag

# Initialise variables
dataPinShiftRegisterOne = 18
sendOutPinShiftRegisterOne = 23
clockPinShiftRegisterOne = 24
resetPinShiftRegisterOne = 25

dataPinShiftRegisterTwo = 17
sendOutPinShiftRegisterTwo = 27
clockPinShiftRegisterTwo = 22
resetPinShiftRegisterTwo = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(dataPinShiftRegisterOne, GPIO.OUT)
GPIO.setup(sendOutPinShiftRegisterOne, GPIO.OUT)
GPIO.setup(clockPinShiftRegisterOne, GPIO.OUT)
GPIO.setup(resetPinShiftRegisterOne, GPIO.OUT)

GPIO.setup(dataPinShiftRegisterTwo, GPIO.OUT)
GPIO.setup(sendOutPinShiftRegisterTwo, GPIO.OUT)
GPIO.setup(clockPinShiftRegisterTwo, GPIO.OUT)
GPIO.setup(resetPinShiftRegisterTwo, GPIO.OUT)

defaultRowPositions = [9, 14, 8, 12, 1, 7, 2, 5]
defaultColumnPositions = [13, 3, 4, 10, 6, 11, 15, 16]

# UI
root = tk.Tk()
rows, columns = 8, 8
btnMatrix = [[0 for x in range(rows)] for y in range(columns)]
matrix = [[0 for x in range(rows)] for y in range(columns)]


def reset_shift_registers():
    GPIO.output(dataPinShiftRegisterOne, GPIO.LOW)
    GPIO.output(clockPinShiftRegisterOne, GPIO.LOW)
    GPIO.output(resetPinShiftRegisterOne, GPIO.LOW)
    GPIO.output(sendOutPinShiftRegisterOne, GPIO.LOW)
    GPIO.output(dataPinShiftRegisterTwo, GPIO.LOW)
    GPIO.output(clockPinShiftRegisterTwo, GPIO.LOW)
    GPIO.output(resetPinShiftRegisterTwo, GPIO.LOW)
    GPIO.output(sendOutPinShiftRegisterTwo, GPIO.LOW)
    send_data_out()
    GPIO.output(resetPinShiftRegisterOne, GPIO.HIGH)
    GPIO.output(resetPinShiftRegisterTwo, GPIO.HIGH)


def send_data_out():
    GPIO.output(sendOutPinShiftRegisterOne, GPIO.HIGH)
    GPIO.output(sendOutPinShiftRegisterOne, GPIO.LOW)
    GPIO.output(sendOutPinShiftRegisterTwo, GPIO.HIGH)
    GPIO.output(sendOutPinShiftRegisterTwo, GPIO.LOW)


def add_data_to_register(register_number, value):
    if register_number == 1:
        GPIO.output(dataPinShiftRegisterOne, value)
        GPIO.output(clockPinShiftRegisterOne, GPIO.HIGH)
        GPIO.output(clockPinShiftRegisterOne, GPIO.LOW)
        GPIO.output(dataPinShiftRegisterOne, GPIO.LOW)
    else:
        GPIO.output(dataPinShiftRegisterTwo, value)
        GPIO.output(clockPinShiftRegisterTwo, GPIO.HIGH)
        GPIO.output(clockPinShiftRegisterTwo, GPIO.LOW)
        GPIO.output(dataPinShiftRegisterTwo, GPIO.LOW)


def draw_matrix(matrix_to_draw):
    for rowIndex, row in enumerate(matrix_to_draw):
        register_one = [0, 0, 0, 0, 0, 0, 0, 0]
        register_two = [0, 0, 0, 0, 0, 0, 0, 0]
        for columnIndex, valueToSend in enumerate(matrix_to_draw[rowIndex]):
            default_row_position = defaultRowPositions[rowIndex]
            default_column_position = defaultColumnPositions[columnIndex]
            if valueToSend == 1:
                if default_row_position <= 8:
                    register_one[default_row_position - 1] = 1
                else:
                    register_two[default_row_position - 9] = 1
                if default_column_position <= 8:
                    register_one[default_column_position - 1] = 0
                else:
                    register_two[default_column_position - 9] = 0
            else:
                if default_column_position <= 8:
                    register_one[default_column_position - 1] = 1
                else:
                    register_two[default_column_position - 9] = 1

        for x in reversed(register_one):
            add_data_to_register(1, x)
        for y in register_two:
            add_data_to_register(2, y)
        send_data_out()


def close_window():
    reset_shift_registers()
    root.destroy()


def button_grid_click(row_number, column_number):
    btn_text = btnMatrix[row_number][column_number]["text"]
    if btn_text == "0":
        btnMatrix[row_number][column_number].config(bg="red", text="1")
    else:
        btnMatrix[row_number][column_number].config(bg="lightgray", text="0")


def button_stop_click():
    global runGrid
    runGrid = False
    global testAll
    testAll = False
    reset_shift_registers()


def button_send_click():
    global matrix
    matrix = reset_matrix()
    for rowIndex, row in enumerate(btnMatrix):
        for columnIndex, btn in enumerate(btnMatrix[rowIndex]):
            if btn["text"] == "0":
                matrix[rowIndex][columnIndex] = 0
            else:
                matrix[rowIndex][columnIndex] = 1
    global runGrid
    runGrid = True


def button_testall_click():
    global testAll
    testAll = True


def reset_matrix():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


# start main program
root.protocol("WM_DELETE_WINDOW", close_window)
reset_shift_registers()

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)
bottom_frame = tk.Frame(root).pack(side="bottom")

for rowNumber in range(8):
    for columnNumber in range(8):
        btnMatrix[rowNumber][columnNumber] = tk.Button(top_frame, text="0", bg="lightgray",
                                                       command=lambda x1=rowNumber, y1=columnNumber: button_grid_click(
                                                           x1, y1), height=1, width=4)
        btnMatrix[rowNumber][columnNumber].grid(row=rowNumber, column=columnNumber)

tk.Button(bottom_frame, text="Send", bg="darkgreen", fg="white", height=1, width=5, command=button_send_click).pack()
tk.Button(bottom_frame, text="Stop", bg="darkred", fg="white", height=1, width=5, command=button_stop_click).pack()
tk.Button(bottom_frame, text="TestAll", bg="Black", fg="white", height=1, width=5, command=button_testall_click).pack()

all_characters_length = len(all_characters)

counter = 0
iteration = 0

while True:
    if idx % 500 == 0:
        root.update()
    if runGrid:
        draw_matrix(matrix)
        idx += 1
    if testAll:
        for index, character in enumerate(all_characters):
            iteration = iteration + 1
            draw_matrix(all_characters[counter])
            if iteration == 1000:
                iteration = 0
                counter = counter + 1
                if counter >= (all_characters_length - 1):
                    counter = 0
