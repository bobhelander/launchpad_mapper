"""
systems_button_group.py
Control for a group of buttons that will take intensity away from the other buttons.

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


class SystemsButtonGroup(object):
    """
    SystemsButtonGroup: Control for a group of buttons that will take intensity away from the other buttons.
    """

    def __init__(self, systems_button, weapons_button, engines_button, reset_button):
        self.systems_button = systems_button
        self.weapons_button = weapons_button
        self.engines_button = engines_button
        self.reset_button = reset_button

        self.systems_button.red = 0

        self.systems_button.set_pressed_callback(self.systems_button_pressed)
        self.weapons_button.set_pressed_callback(self.weapons_button_pressed)
        self.engines_button.set_pressed_callback(self.engines_button_pressed)
        self.reset_button.set_pressed_callback(self.reset_button_pressed)

        # I don't want to use half pips
        self.systems_pip = 4
        self.weapons_pip = 4
        self.engines_pip = 4
        self.update_colors()

    def reallocate_pips(self, module_in, module_1_out, module_2_out):
        """
        Take pips from the two "out" modules and add them to the "in" module
        Returns the new module pip counts
        """
        pips_removed = 0

        # Keep taking if there are pips to take
        while pips_removed < 2 and (module_1_out or module_2_out) and (module_in + pips_removed < 8):
            if module_1_out > 0:
                module_1_out -= 1
                pips_removed += 1
            if module_in + pips_removed >= 8:
                break  # Don't allow > 8 pips
            if module_2_out > 0:
                module_2_out -= 1
                pips_removed += 1

        module_in += pips_removed
        return module_in, module_1_out, module_2_out

    def get_color(self, pip_count):
        # Red: pip == 0 = Brightest
        if pip_count <= 2:
            return 3-pip_count, 0
        if pip_count == 3:
            return 3, 3  # Bright Yellow
        if pip_count == 4:
            return 2, 2  # Medium Yellow
        if pip_count == 5:
            return 1, 1  # Low Yellow
        # Green: pip == 8 = Brightest
        if 5 < pip_count <= 8:
            return 0, pip_count - 5

    def update_colors(self):
        self.systems_button.red, self.systems_button.green = self.get_color(self.systems_pip)
        self.weapons_button.red, self.weapons_button.green = self.get_color(self.weapons_pip)
        self.engines_button.red, self.engines_button.green = self.get_color(self.engines_pip)

    def systems_button_pressed(self):
        self.systems_pip, self.weapons_pip, self.engines_pip = self.reallocate_pips(self.systems_pip,
                                                                                    self.weapons_pip,
                                                                                    self.engines_pip)
        self.update_colors()

    def weapons_button_pressed(self):
        self.weapons_pip, self.systems_pip, self.engines_pip = self.reallocate_pips(self.weapons_pip,
                                                                                    self.systems_pip,
                                                                                    self.engines_pip)
        self.update_colors()

    def engines_button_pressed(self):
        self.engines_pip, self.systems_pip, self.weapons_pip = self.reallocate_pips(self.engines_pip,
                                                                                    self.systems_pip,
                                                                                    self.weapons_pip)
        self.update_colors()

    def reset_button_pressed(self):
        self.systems_pip = 4
        self.weapons_pip = 4
        self.engines_pip = 4
        self.update_colors()