/*
keyboard_mapper.ino
Program to read serial commands from the programming port and output
keyboard actions on the native USB port.  Ardunio Due

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
*/

char readBuffer[2];
  // initialize serial:
  Serial.begin(9600);
  Keyboard.begin();
}

void serialEvent() {
  while (Serial.available()) {
    // get the new bytes:
    int count = Serial.readBytes(readBuffer, 2);
    if (count == 2) {
      char releaseChar = (char)readBuffer[0];
      char pressChar = (char)readBuffer[1];
       
      if (releaseChar != 0) {
        //Keyboard.println("release");
        Keyboard.release(releaseChar);
      }
      if (pressChar != 0) {
        //Keyboard.println("press");
        Keyboard.press(pressChar);
      }
      if (releaseChar == 0 && pressChar == 0) {
        Keyboard.releaseAll();
      }
    }
  }
}

void loop() {
  // Just waiting for serial events
}
