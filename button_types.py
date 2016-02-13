"""
button_types.py
Implementation of various button types for the launchpad mapper program.

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


class ShutdownException(Exception):
    """
    ShutdownException: Raised to interrupt the main loop.
    """
    pass


class ButtonKey(object):
    """
    ButtonKey:  Base class for all the button types.
    """

    def __init__(self, x, y, description=""):
        self._x = x
        self._y = y
        self.description = description

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def pressed(self, launchpad, arduino):
        """
        Button has been pressed.  Default implementation turns on the red LED

        Parameters:
        launchpad  Launchpad object
        arduino  Keyboard handler
        """
        launchpad.LedCtrlXY(self.x, self.y, 0, 3)

    def released(self, launchpad, arduino):
        """
        Button has been released.  Default implementation turns off all LEDs.

        Parameters:
        launchpad  Launchpad object
        arduino  Keyboard handler
        """
        launchpad.LedCtrlXY(self.x, self.y, 0, 0)

    def draw(self, launchpad, color_value):
        """
        Called every cycle.  About .1 seconds

        Parameters:
        launchpad  Launchpad object
        color_value  A value from 0-3 that cycles though the values.  Useful for
                     a flashing LED.
        """
        pass


class ShutdownButton(ButtonKey):
    """
    ShutdownButton: Raised the ShutdownException when pressed.
    """

    def __init__(self, x, y, description=""):
        super(ShutdownButton, self).__init__(x, y, description=description)

    def pressed(self, launchpad, port):
        raise ShutdownException("Shutdown")

    def released(self, launchpad, port):
        pass


class InputButton(ButtonKey):
    """
    InputButton: Button type to report a key down while the button is pressed.

    Initialization parameters:
    x - X position of the button on the launchpad (0-8)
    y - Y position of the button on the launchpad (0-8)
    red - Intensity of the red LED while the button is not pressed (0-3).  Default 0
    green - Intensity of the green LED while the button is not pressed (0-3).  Default 0
    pressed_red - Intensity of the red LED while the button is pressed (0-3).  Default 3
    pressed_green - Intensity of the green LED while the button is pressed (0-3).  Default 0
    key_output - The key that will be reported as down while the button is pressed.  Default None
    flashing - True if the button is to cycle the pressed colors while the button is pressed.  Default False.
    """

    def __init__(self, x, y, red=0, green=0, pressed_red=3, pressed_green=0,
                 key_output=None, flashing=False, description=""):
        super(InputButton, self).__init__(x, y, description=description)
        self._red = red
        self._green = green
        self.pressed_red = pressed_red
        self.pressed_green = pressed_green
        self.key_output = key_output
        self._pressed = False
        self.flashing = flashing
        self._pressed_callback = None

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        self._green = value

    def set_pressed_callback(self, method):
        """
        Sets a method to be called when this button is pressed
        """
        self._pressed_callback = method

    def pressed(self, launchpad, arduino):
        try:
            if self._pressed_callback:
                self._pressed_callback()
            if self.key_output and not self._pressed:
                arduino.key_down(self.key_output)
        finally:
            self._pressed = True

    def released(self, launchpad, arduino):
        try:
            if self.key_output and self._pressed:
                arduino.key_release(self.key_output)
        finally:
            self._pressed = False

    def draw(self, launchpad, color_value):
        if self._pressed:
            if self.flashing:
                # Use the cycling color_value if the pressed color is not zero
                launchpad.LedCtrlXY(self.x, self.y,
                                    color_value if self.pressed_red else 0,
                                    color_value if self.pressed_green else 0)
            else:
                launchpad.LedCtrlXY(self.x, self.y, self.pressed_red, self.pressed_green)
        else:
            launchpad.LedCtrlXY(self.x, self.y, self._red, self._green)


class FlashingButton(ButtonKey):
    """
    FlashingButton:  Simple button that flashes while pressed
    """

    def __init__(self, x, y, description=""):
        super(FlashingButton, self).__init__(x, y, description=description)
        self._pressed = False

    def pressed(self, launchpad, arduino):
        self._pressed = True

    def released(self, launchpad, arduino):
        self._pressed = False

    def draw(self, launchpad, color_value):
        if self._pressed:
            launchpad.LedCtrlXY(self.x, self.y, color_value, 0)
        else:
            launchpad.LedCtrlXY(self.x, self.y, 0, 0)


class ToggleButton(ButtonKey):
    """
    ToggleButton: Button that can send a keypress when the button is toggled on/off.

    Initialization parameters:
    x - X position of the button on the launchpad (0-8)
    y - Y position of the button on the launchpad (0-8)
    red - Intensity of the red LED while the button is toggled off (0-3).  Default 0
    green - Intensity of the green LED while the button is toggled off (0-3).  Default 0
    toggled_red - Intensity of the red LED while the button is toggled on (0-3).  Default 3
    toggled_green - Intensity of the green LED while the button is toggled on (0-3).  Default 0
    key_output_set - The key that will pressed (down/up) when the button is toggled on.  Default None
    key_output_cleared - The key that will pressed (down/up) when the button is toggled off.  Default None
    flashing - True if the button is to cycle the toggled colors while the button toggled on.  Default False.
    key_duration - The amount of time the key will be held down for the keypress.  Default .2
    """

    def __init__(self, x, y, red=0, green=3, toggled_red=3, toggled_green=0,
                 key_output_set=None, key_output_cleared=None, flashing=False, key_duration=.2,
                 description=""):
        super(ToggleButton, self).__init__(x, y, description=description)
        self._toggled = False
        self.red = red
        self.green = green
        self.toggled_red = toggled_red
        self.toggled_green = toggled_green
        self.key_output_set = key_output_set
        self.key_output_cleared = key_output_cleared
        self.flashing = flashing
        self.key_duration = key_duration

    def pressed(self, launchpad, arduino):
        self._toggled = not self._toggled
        if self.key_output_set and self._toggled:
            arduino.key_press(self.key_output_set, self.key_duration)
        if self.key_output_cleared and not self._toggled:
            arduino.key_press(self.key_output_cleared, self.key_duration)

    def released(self, launchpad, arduino):
        pass

    def draw(self, launchpad, color_value):
        if self._toggled:
            if self.flashing:
                launchpad.LedCtrlXY(self.x, self.y,
                                    color_value if self.toggled_red else 0,
                                    color_value if self.toggled_green else 0)
            else:
                launchpad.LedCtrlXY(self.x, self.y, self.toggled_red, self.toggled_green)
        else:
            launchpad.LedCtrlXY(self.x, self.y, self.red, self.green)


