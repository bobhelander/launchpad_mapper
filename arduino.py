"""
arduino.py
Provides the Arduino class for wrapping the communication to the arduino board

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

import serial
from time import sleep


class Arduino(object):
    """
    Wrapper for the communication to the arduino board
    """

    def __init__(self, comm_port, baud_rate=9600):
        self.port = serial.Serial(comm_port, baud_rate)

    def key_down(self, key):
        """
        Tell the board to send the USB key down
        """
        self.port.write([key, 0x00])

    def key_release(self, key):
        """
        Tell the board to release a key
        """
        self.port.write([0x00, key])

    def key_press(self, key, duration):
        """
        Tell the board to press and release a key
        """
        self.port.write([key, 0x00])
        sleep(duration)
        self.port.write([0x00, key])