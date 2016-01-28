"""
launchpad_mapper.py
Program to allow mapping of the Novation Launchpad buttons to USB keystrokes.

Copyright (C) 2016  Bob Helander

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
from launchpad import Launchpad
from button_types import ShutdownException, ButtonKey, ToggleButton, InputButton
from systems_button_group import SystemsButtonGroup
from arduino import Arduino
from itertools import chain


def handle_event(launchpad, arduino, button_key, button_pressed):
    """
    Call the method on the button type to handle the event
    """

    if button_pressed:
        button_key.pressed(launchpad, arduino)
    else:
        button_key.released(launchpad, arduino)


def color_cycle():
    """
    Returns a value that cycles between 0 and 3
    """
    # Get ticks as an integer
    ticks = int(float('%0.3f' % time.time()) * 1000)
    # Only use < 1000
    millisecond = ticks % 1000
    # Counting up in the first half of the second and down the other half
    count_down = (millisecond / 500)
    # 0-150 = 3 151-300 = 2 301-450 = 1 451-499 = 0 500-650 = 0 651-800 = 1 801-950 = 2 951-999 = 3
    return int((millisecond - 500) / 150) if count_down else 3 - millisecond / 150


def setup(pad_state):
    """
    Add the mapped buttons to the pad_state array (Elite Dangerous)
    """

    #ESC
    pad_state[0][0] = InputButton(0, 0, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0xB1,  # ESC
                                  flashing=True)

    #FSD
    pad_state[8][1] = InputButton(8, 1, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6A,  # KEY_J,
                                  flashing=True)

    #Landing Gear
    pad_state[7][1] = ToggleButton(7, 1, red=0, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0xD1,  # Insert,
                                   key_output_cleared=0xD1, flashing=True)

    #Landing Lights
    pad_state[6][1] = ToggleButton(6, 1, red=0, green=3, toggled_red=3, toggled_green=3,
                                   key_output_set=0xD4,  # Delete
                                   key_output_cleared=0xD4, flashing=True)

    #75% Speed
    pad_state[8][3] = InputButton(8, 3, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2C,  # Comma
                                  flashing=False)
    #50% Speed
    pad_state[8][4] = InputButton(8, 4, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2E,  # Period
                                  flashing=False)
    #0% Speed
    pad_state[8][5] = InputButton(8, 5, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x78,  # KEY_X,
                                  flashing=False)
    #Communications Panel
    pad_state[0][7] = InputButton(0, 7, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x32,  # KEY_2,
                                  flashing=False)
    #Target Panel
    pad_state[0][8] = InputButton(0, 8, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x31,  # KEY_1,
                                  flashing=False)
    #Systems Panel
    pad_state[1][8] = InputButton(1, 8, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x34,  # KEY_4,
                                  flashing=False)
    #Galaxy Map
    pad_state[0][6] = InputButton(0, 6, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x69,  # KEY_I,
                                  flashing=False)
    #System Map
    pad_state[1][6] = InputButton(1, 6, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6F,  # KEY_O
                                  flashing=False)

    # W
    pad_state[1][3] = InputButton(1, 3, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x77,  # KEY_W,
                                  flashing=False)
    # A
    pad_state[0][4] = InputButton(0, 4, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x61,  # KEY_A,
                                  flashing=False)
    # S
    pad_state[1][5] = InputButton(1, 5, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x73,  # KEY_S,
                                  flashing=False)
    # D
    pad_state[2][4] = InputButton(2, 4, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x64,  # KEY_D,
                                  flashing=False)
    #Select
    pad_state[1][4] = InputButton(1, 4, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x20,  # VK_SPACE,
                                  flashing=False)
    #Previous Tab
    pad_state[0][3] = InputButton(0, 3, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x71,  # KEY_Q,
                                  flashing=False)
    #Next Tab
    pad_state[2][3] = InputButton(2, 3, red=1, green=202, pressed_red=3, pressed_green=0,
                                  key_output=0x65,  # KEY_E,
                                  flashing=False)

    #Engines
    pad_state[5][4] = InputButton(5, 4, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xDA,  # Up Arrow
                                  flashing=False)
    #Systems
    pad_state[4][5] = InputButton(4, 5, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xD8,  # Left Arrow
                                  flashing=False)
    #Weapons
    pad_state[6][5] = InputButton(6, 5, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xD7,  # Right arrow
                                  flashing=False)
    #Reset
    pad_state[5][5] = InputButton(5, 5, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0xD9,  # Down arrow
                                  flashing=False)

    # callback mappings will keep this object from being garbage collected
    _ = SystemsButtonGroup(systems_button=pad_state[4][5],
                           weapons_button=pad_state[6][5],
                           engines_button=pad_state[5][4],
                           reset_button=pad_state[5][5])

    #Hardpoints
    pad_state[8][6] = ToggleButton(8, 6, red=0, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0x75,  # KEY_U,
                                   key_output_cleared=0x75, flashing=True)
    #Next Weapon Group
    pad_state[8][7] = InputButton(8, 7, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6E,  # KEY_N,
                                  flashing=False)
    #Previous Weapon Group
    pad_state[8][8] = InputButton(8, 8, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6D,  # KEY_M,
                                  flashing=False)
    #Wingman's Target
    pad_state[7][6] = InputButton(7, 6, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x30,  # KEY_0,
                                  flashing=False)
    #Front Target
    pad_state[7][7] = InputButton(7, 7, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x74,  # KEY_T,
                                  flashing=False)
    #Most Threatening Target
    pad_state[7][8] = InputButton(7, 8, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x68,  # KEY_H,
                                  flashing=False)
    #Next Target
    pad_state[6][7] = InputButton(6, 7, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x67,  # KEY_G,
                                  flashing=False)
    #Previous Target
    pad_state[6][8] = InputButton(6, 8, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x66,  # KEY_F,
                                  flashing=False)
    #Next Target Subsystem
    pad_state[5][7] = InputButton(5, 7, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x79,  # KEY_Y,
                                  flashing=False)
    #Previous Target Subsystem
    pad_state[5][8] = InputButton(5, 8, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x63,  # KEY_C,
                                  flashing=False)

    #Increase Sensor Range
    pad_state[3][7] = InputButton(3, 7, red=1, green=2, pressed_red=0, pressed_green=3,
                                  key_output=0xD3,  # Page Up
                                  flashing=False)
    #Decrease Sensor Range
    pad_state[3][8] = InputButton(3, 8, red=1, green=2, pressed_red=0, pressed_green=3,
                                  key_output=0xD6,  # Page Down
                                  flashing=False)
    #Flight Assist
    pad_state[4][0] = ToggleButton(4, 0, red=3, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0x7A,  # KEY_Z,
                                   key_output_cleared=0x7A, flashing=True)
    #Hyperspace
    pad_state[7][0] = InputButton(7, 0, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x2B,  # Add
                                  flashing=True)
    #Supercruise
    pad_state[6][0] = InputButton(6, 0, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x2A,  # Multiply
                                  flashing=True)

    #Wingman 1
    pad_state[0][1] = InputButton(0, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x37,  # KEY_7,
                                  flashing=False)
    #Wingman 2
    pad_state[1][1] = InputButton(1, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x38,  # KEY_8,
                                  flashing=False)
    #Wingman 3
    pad_state[2][1] = InputButton(2, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x39,  # KEY_9,
                                  flashing=False)
    #Wingman Nav-Lock
    pad_state[3][1] = InputButton(3, 1, red=2, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2D,  # Minus
                                  flashing=False)

    #Cargo Scoop
    pad_state[6][2] = ToggleButton(6, 2, red=3, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0xD2,  # Home
                                   key_output_cleared=0xD2, flashing=True)
    #Jettison Cargo
    pad_state[4][2] = InputButton(4, 2, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0xD5,  # End
                                  flashing=False)


def main():
    launchpad = Launchpad()  # create a Launchpad instance
    launchpad.Open()         # start it

    try:
        # Open communication to the Arduino
        arduino = Arduino('COM6', 9600)

        # Prepare the 9X9 array of buttons to the list
        pad_state = [[ButtonKey(x, y) for x in range(0, 9)] for y in range(0, 9)]

        # Update the array with the buttons that are mapped
        setup(pad_state)

        try:
            while True:
                color_value = color_cycle()

                # Update the display
                for button in chain(pad_state):
                    button.draw(launchpad, color_value)

                # Check for button event
                button_event = launchpad.ButtonStateXY()
                if button_event:
                    handle_event(launchpad=launchpad,
                                 arduino=arduino,
                                 button_key=pad_state[button_event[0]][button_event[1]],
                                 button_pressed=button_event[2])
                    continue

                time.sleep(.1)

                arduino.key_release(0x00) # Release all keys

        except ShutdownException, _ex:
            pass
        except Exception, ex:
            print ex

    finally:
        launchpad.Reset()
        launchpad.Close()


if __name__ == '__main__':
    main()