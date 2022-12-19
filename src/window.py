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

from .inscriptions.bilge_khagan.bilge_khagan_page import PageBilgeKhagan
from .inscriptions.kul_tigin.kul_tigin_page import PageKulTigin
from .inscriptions.tonyukuk.tonyukuk_page import PageTonyukuk


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/window.ui')
class RootiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RootiWindow'

    cb_old = Gtk.Template.Child("cb_old")
    cb_phonologic = Gtk.Template.Child("cb_phonologic")
    cb_modern = Gtk.Template.Child("cb_modern")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cb_old.connect("toggled", self.visible_old)
        self.cb_phonologic.connect("toggled", self.visible_phonologic)
        self.cb_modern.connect("toggled", self.visible_modern)

        self.cb_old.set_active(True)
        for openclose in (1, 0):
            self.cb_phonologic.set_active(openclose)
            self.cb_modern.set_active(openclose)

    def visible_old(self, button):
        """Sets old widgets visibility to the given button state."""
        check = button.get_active()

    def visible_phonologic(self, button):
        """Sets phonologic widgets visibility to the given button state."""
        check = button.get_active()

    def visible_modern(self, button):
        """Sets modern widgets visibility to the given button state."""
        check = button.get_active()
