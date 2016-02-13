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
from button_types import ShutdownException, ButtonKey
from elite_mapping import setup_ship
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



def main():
    launchpad = Launchpad()  # create a Launchpad instance
    launchpad.Open()         # start it

    try:
        # Open communication to the Arduino
        arduino = Arduino('COM6', 9600)

        pad_states = list()

        # Prepare the 9X9 array of buttons to the list
        pad_states.append([[ButtonKey(x, y) for y in range(0, 9)] for x in range(0, 9)])

        # Update the array with the buttons that are mapped
        setup_ship(pad_states[0])

        current_pad_state = pad_states[0]

        try:
            while True:
                color_value = color_cycle()

                # Update the display
                for button in chain(*current_pad_state):  # Flatten out the 2d array
                    button.draw(launchpad, color_value)

                # Check for button event
                button_event = launchpad.ButtonStateXY()
                if button_event:
                    handle_event(launchpad=launchpad,
                                 arduino=arduino,
                                 button_key=current_pad_state[button_event[0]][button_event[1]],
                                 button_pressed=button_event[2])
                    continue

                time.sleep(.1)

                arduino.key_release(0x00)  # Release all keys

        except ShutdownException, _ex:
            pass
        except Exception, ex:
            print ex

    finally:
        launchpad.Reset()
        launchpad.Close()


if __name__ == '__main__':
    main()