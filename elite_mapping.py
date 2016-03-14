"""
elite_mapping.py
Setup for the Elite control mapping.

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

from button_types import ToggleButton, InputButton, PadPageButton, FlashingButton
from systems_button_group import SystemsButtonGroup


def setup_ship(pad_state):
    """
    Add the mapped buttons to the pad_state array (Elite Dangerous)
    """

    #ESC
    pad_state[0][0] = InputButton(0, 0, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0xB1,  # ESC
                                  flashing=True, description="ESC")
    #Change page
    pad_state[1][0] = PadPageButton(1, 0, red=0, green=3, page=1, description="Change Page 1")

    #Deploy Heat Sink
    pad_state[2][0] = InputButton(2, 0, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x76,  # KEY_V
                                  flashing=True, description="Heat Sink")
    #Chaff
    pad_state[3][0] = InputButton(3, 0, red=3, green=3, pressed_red=3, pressed_green=3,
                                  key_output=0xCA,  # F9
                                  flashing=True, description="Chaff")
    #Deploy Shield Cell
    pad_state[4][0] = InputButton(4, 0, red=0, green=3, pressed_red=3, pressed_green=3,
                                  key_output=0xCB,  # F10
                                  flashing=True, description="Shield Cell")
    #Flight Assist
    pad_state[5][0] = ToggleButton(5, 0, red=3, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0x7A,  # KEY_Z,
                                   key_output_cleared=0x7A, flashing=True, description="Flight Assist")
    #FSD
    pad_state[8][1] = InputButton(8, 1, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6A,  # KEY_J,
                                  flashing=True, description="FSD")

    #Landing Gear
    pad_state[7][1] = ToggleButton(7, 1, red=0, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0xD1,  # Insert,
                                   key_output_cleared=0xD1, flashing=True, description="Gear")

    #Landing Lights
    pad_state[6][1] = ToggleButton(6, 1, red=0, green=3, toggled_red=3, toggled_green=3,
                                   key_output_set=0xD4,  # Delete
                                   key_output_cleared=0xD4, flashing=True, description="Lights")

    #75% Speed
    pad_state[8][3] = InputButton(8, 3, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2C,  # Comma
                                  flashing=False, description="75%")
    #50% Speed
    pad_state[8][4] = InputButton(8, 4, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2E,  # Period
                                  flashing=False, description="50%")
    #0% Speed
    pad_state[8][5] = InputButton(8, 5, red=3, green=0, pressed_red=3, pressed_green=0,
                                  key_output=0x78,  # KEY_X,
                                  flashing=False, description="0%")
    #Communications Panel
    pad_state[0][1] = InputButton(0, 1, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x32,  # KEY_2,
                                  flashing=False, description="Comms")
    #Target Panel
    pad_state[0][7] = InputButton(0, 7, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x31,  # KEY_1,
                                  flashing=False, description="Target Panel")
    #Systems Panel
    pad_state[2][7] = InputButton(2, 7, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x34,  # KEY_4,
                                  flashing=False, description="Systems Panel")
    #Sensors Panel
    pad_state[1][8] = InputButton(1, 8, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x33,  # KEY_3,
                                  flashing=False, description="Role Panel")
    #Galaxy Map
    pad_state[0][3] = InputButton(0, 3, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x69,  # KEY_I,
                                  flashing=False, description="Galaxy Map")
    #System Map
    pad_state[1][3] = InputButton(1, 3, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6F,  # KEY_O
                                  flashing=False, description="System Map")


    # W
    pad_state[1][5] = InputButton(1, 5, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x77,  # KEY_W,
                                  flashing=False, description="Up")
    # A
    pad_state[0][6] = InputButton(0, 6, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x61,  # KEY_A,
                                  flashing=False, description="Left")
    # S
    pad_state[1][7] = InputButton(1, 7, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x73,  # KEY_S,
                                  flashing=False, description="Down")
    # D
    pad_state[2][6] = InputButton(2, 6, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0x64,  # KEY_D,
                                  flashing=False, description="Right")
    #Select
    pad_state[1][6] = InputButton(1, 6, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x20,  # VK_SPACE,
                                  flashing=False, description="Select")
    #Previous Tab
    pad_state[0][5] = InputButton(0, 5, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x71,  # KEY_Q,
                                  flashing=False, description="Previous")
    #Next Tab
    pad_state[2][5] = InputButton(2, 5, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x65,  # KEY_E,
                                  flashing=False, description="Next")

    #Engines
    pad_state[5][4] = InputButton(5, 4, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xDA,  # Up Arrow
                                  flashing=False, description="Engines")
    #Systems
    pad_state[4][5] = InputButton(4, 5, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xD8,  # Left Arrow
                                  flashing=False, description="Systems")
    #Weapons
    pad_state[6][5] = InputButton(6, 5, red=3, green=0, pressed_red=0, pressed_green=3,
                                  key_output=0xD7,  # Right arrow
                                  flashing=False, description="Weapons")
    #Reset
    pad_state[5][5] = InputButton(5, 5, red=3, green=3, pressed_red=0, pressed_green=3,
                                  key_output=0xD9,  # Down arrow
                                  flashing=False, description="Reset")

    # callback mappings will keep this object from being garbage collected
    _ = SystemsButtonGroup(systems_button=pad_state[4][5],
                           weapons_button=pad_state[6][5],
                           engines_button=pad_state[5][4],
                           reset_button=pad_state[5][5])

    #Hardpoints
    pad_state[8][6] = ToggleButton(8, 6, red=0, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0x75,  # KEY_U,
                                   key_output_cleared=0x75, flashing=True, description="Hardpoints")
    #Next Weapon Group
    pad_state[8][7] = InputButton(8, 7, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6E,  # KEY_N,
                                  flashing=False, description="Next Weapon Group")
    #Previous Weapon Group
    pad_state[8][8] = InputButton(8, 8, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x6D,  # KEY_M,
                                  flashing=False, description="Previous Weapon Group")
    #Wingman's Target
    pad_state[7][6] = InputButton(7, 6, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x30,  # KEY_0,
                                  flashing=False, description="Wingman Target")
    #Front Target
    pad_state[7][7] = InputButton(7, 7, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x74,  # KEY_T,
                                  flashing=False, description="Front Target")
    #Most Threatening Target
    pad_state[7][8] = InputButton(7, 8, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x68,  # KEY_H,
                                  flashing=False, description="Most Threatening Target")
    #Next Target
    pad_state[6][7] = InputButton(6, 7, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x67,  # KEY_G,
                                  flashing=False, description="Next Target")
    #Previous Target
    pad_state[6][8] = InputButton(6, 8, red=3, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x66,  # KEY_F,
                                  flashing=False, description="Previous Target")
    #Next Target Subsystem
    pad_state[5][7] = InputButton(5, 7, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x79,  # KEY_Y,
                                  flashing=False, description="Next Subsystem")
    #Previous Target Subsystem
    pad_state[5][8] = InputButton(5, 8, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0x63,  # KEY_C,
                                  flashing=False, description="Previous Subsystem")

    #Increase Sensor Range
    pad_state[3][7] = InputButton(3, 7, red=1, green=2, pressed_red=0, pressed_green=3,
                                  key_output=0xD3,  # Page Up
                                  flashing=False, description="Increase Range")
    #Decrease Sensor Range
    pad_state[3][8] = InputButton(3, 8, red=1, green=2, pressed_red=0, pressed_green=3,
                                  key_output=0xD6,  # Page Down
                                  flashing=False, description="Decrease Range")
    #Hyperspace
    pad_state[7][0] = InputButton(7, 0, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x2B,  # Add
                                  flashing=True, description="Hyperspace")
    #Supercruise
    pad_state[6][0] = InputButton(6, 0, red=1, green=2, pressed_red=3, pressed_green=0,
                                  key_output=0x2A,  # Multiply
                                  flashing=True, description="Supercruise")

    #Wingman 1
    pad_state[1][1] = InputButton(1, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x37,  # KEY_7,
                                  flashing=False, description="Wingman 1")
    #Wingman 2
    pad_state[2][1] = InputButton(2, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x38,  # KEY_8,
                                  flashing=False, description="Wingman 2")
    #Wingman 3
    pad_state[3][1] = InputButton(3, 1, red=0, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x39,  # KEY_9,
                                  flashing=False, description="Wingman 3")
    #Wingman Nav-Lock
    pad_state[4][1] = InputButton(4, 1, red=2, green=3, pressed_red=3, pressed_green=0,
                                  key_output=0x2D,  # Minus
                                  flashing=False, description="Winman Nav-Lock")

    #Cargo Scoop
    pad_state[6][2] = ToggleButton(6, 2, red=3, green=3, toggled_red=3, toggled_green=0,
                                   key_output_set=0xD2,  # Home
                                   key_output_cleared=0xD2, flashing=True, description="Cargo Scoop")
    #Silent Running
    pad_state[7][2] = ToggleButton(7, 2, red=3, green=0, toggled_red=3, toggled_green=3,
                                   key_output_set=0xCC,  # F11
                                   key_output_cleared=0xCC, flashing=True, description="Silent Running")
    #Jettison Cargo
    pad_state[4][2] = InputButton(4, 2, red=3, green=0, pressed_red=3, pressed_green=3,
                                  key_output=0xD5,  # End
                                  flashing=False, description="Jettison Cargo")



