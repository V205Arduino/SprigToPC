"""
SprigToPC:
Send keystrokes from a Sprig to a computer.
Can be used for playing Sprig games on a computer while using a Sprig as a console.
REQUIRED HARDWARE:
* Sprig Console with pico flashed with circuitPython Display is optional right now though I plan to add it in the future.
"""


import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("Hello World! From SprigToPC")


""" SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries, Modified by V205 to adapt it to a Sprig console

SPDX-License-Identifier: MIT(No clue about this so I will just leave it like that. )

"""
# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# W button
wButton = digitalio.DigitalInOut(board.GP5)
wButton.switch_to_input(pull=digitalio.Pull.UP)

# A button
aButton = digitalio.DigitalInOut(board.GP6)
aButton.switch_to_input(pull=digitalio.Pull.UP)

# S button
sButton = digitalio.DigitalInOut(board.GP7)
sButton.switch_to_input(pull=digitalio.Pull.UP)

# D button
dButton = digitalio.DigitalInOut(board.GP8)
dButton.switch_to_input(pull=digitalio.Pull.UP)

# i button
iButton = digitalio.DigitalInOut(board.GP12)
iButton.switch_to_input(pull=digitalio.Pull.UP)

# J Button
jButton = digitalio.DigitalInOut(board.GP13)
jButton.switch_to_input(pull=digitalio.Pull.UP)

# K button
kButton = digitalio.DigitalInOut(board.GP14)
kButton.switch_to_input(pull=digitalio.Pull.UP)

# L button
lButton = digitalio.DigitalInOut(board.GP15)
lButton.switch_to_input(pull=digitalio.Pull.UP)

# A variable that I didn't really use......
x = 0

# Play around with this. Later I might make it so that you can't hold the button down...
timeBetweenKeystrokes = 0.2
# print("Debug test!")



#def checkButton(buttonstate, Keycode ):
    #todo make better code 

while True:
    # print("loop debug")

    # Check button states
    if not wButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.W)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not aButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.A)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not sButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.S)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not dButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.D)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not iButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.I)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not jButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.J)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not kButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.K)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)

    elif not lButton.value:
        # print("You pressed the button!")
        # print(x)
        kbd.send(Keycode.L)

        x = x + 1
        time.sleep(0.5)  # Write your code here :-)
