# window.py
#
# Copyright 2022 imsi32
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/github/imsi32/RooTi/window.ui')
class RootiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RootiWindow'

    label = Gtk.Template.Child()

    rd_gokturk = Gtk.Template.Child()
    rd_phonologic = Gtk.Template.Child()
    rd_modern = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rd_gokturk.connect("toggled", self.on_gokturk)
        self.rd_phonologic.connect("toggled", self.on_phonologic)
        self.rd_modern.connect("toggled", self.on_modern)

        self.rd_gokturk.set_active(True)

    def on_gokturk(self, button):
        """Sets the visibility to only Gokturk form."""
        self.visible_gokturk(True)
        self.visible_phonologic(False)
        self.visible_modern(False)

    def on_phonologic(self, button):
        """Sets the visibility to only Phonologic form."""
        self.visible_gokturk(False)
        self.visible_phonologic(True)
        self.visible_modern(False)

    def on_modern(self, button):
        """Sets the visibility to only Modern form."""
        self.visible_gokturk(False)
        self.visible_phonologic(False)
        self.visible_modern(True)

    def visible_gokturk(self, boolean):
        """Sets gokturk widgets visibility to the given *boolean*."""
        pass

    def visible_phonologic(self, boolean):
        """Sets phonologic widgets visibility to the given *boolean*."""
        pass

    def visible_modern(self, boolean):
        """Sets modern widgets visibility to the given *boolean*."""
        pass
