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
from trade_extensions import setup_trade
from arduino_mock import Arduino
from itertools import chain
from speech import say


def handle_event(launchpad, arduino, button_key, button_pressed, pad_states, current_pad_state):
    """
    Call the method on the button type to handle the event
    """
    kwargs = {"launchpad": launchpad,
              "arduino": arduino,
              "pad_states": pad_states,
              "current_pad_state": current_pad_state}

    if button_pressed:
        response = button_key.pressed(**kwargs)
        if button_key.description:
            print button_key.description
            say(button_key.description)
    else:
        response = button_key.released(**kwargs)

    return response


def write_changes(launchpad, new_buffer, old_buffer):
    for index in range(0, len(new_buffer)):
        if new_buffer[index] != old_buffer[index]:
            if index > 120:  # Automap buttons
                launchpad.midi.RawWrite(176, 104 + (index - 121), new_buffer[index])
            else:
                launchpad.midi.RawWrite(144, index, new_buffer[index])

            old_buffer[index] = new_buffer[index]


def main():
    launchpad = Launchpad()  # create a Launchpad instance
    launchpad.Open()         # start it
    launchpad_buffer = [0 for _ in range(200)]    # LED color map
    launchpad_buffer_cache = [0 for _ in range(200)]    # LED color map

    # Reset the launchpad
    launchpad.midi.RawWrite(176, 0, 0)

    # Set X/Y Mode
    launchpad.midi.RawWrite(176, 0, 1)

    # Turn Flashing on
    launchpad.midi.RawWrite(176, 0, 40)

    # Control Duty cycle
    # numerator = 16
    # denominator = 4
    # if numerator < 9:
    #     value = (16 * (numerator - 1)) + (denominator - 3)
    #     launchpad.midi.RawWrite(176, 30, value)
    # else:
    #     value = (16 * (numerator - 9)) + (denominator - 3)
    #     launchpad.midi.RawWrite(176, 31, value)

    try:
        # Open communication to the Arduino
        arduino = Arduino('COM6', 9600)

        pad_states = list()

        # Prepare the 9X9 array of buttons to the list
        pad_states.append([[ButtonKey(x, y) for y in range(0, 9)] for x in range(0, 9)])
        # Add another page
        pad_states.append([[ButtonKey(x, y) for y in range(0, 9)] for x in range(0, 9)])

        # Update the array with the buttons that are mapped
        setup_ship(pad_states[0])
        setup_trade(pad_states[1])

        current_pad_state = pad_states[0]

        try:
            while True:
                # Update the display buffer
                for button in chain(*current_pad_state):  # Flatten out the 2d array
                    button.draw(launchpad_buffer_cache)

                # Write the display buffer
                write_changes(launchpad, launchpad_buffer_cache, launchpad_buffer)

                # Check for button event
                button_event = launchpad.ButtonStateXY()
                if button_event:
                    response = handle_event(launchpad=launchpad,
                                            arduino=arduino,
                                            button_key=current_pad_state[button_event[0]][button_event[1]],
                                            button_pressed=button_event[2],
                                            pad_states=pad_states,
                                            current_pad_state=current_pad_state)
                    # Was there a state change
                    if response and "state" in response:
                        current_pad_state = response.get("state")

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