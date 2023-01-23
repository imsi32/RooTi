# bilge_khagan_slide_west.py
#
# Copyright 2022-2023 imsi32
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/bilge_khagan/bilge_khagan_slide_west.ui')
class BilgeKhaganSlideWest(Adw.Bin):
    __gtype_name__ = 'BilgeKhaganSlideWest'

    old_BK_W1 = Gtk.Template.Child("old_BK_W1")
    old_BK_W2 = Gtk.Template.Child("old_BK_W2")
    old_BK_W3 = Gtk.Template.Child("old_BK_W3")
    old_BK_W4 = Gtk.Template.Child("old_BK_W4")
    old_BK_W5 = Gtk.Template.Child("old_BK_W5")
    old_BK_W6 = Gtk.Template.Child("old_BK_W6")
    old_BK_W7 = Gtk.Template.Child("old_BK_W7")
    old_BK_W8 = Gtk.Template.Child("old_BK_W8")
    old_BK_W9 = Gtk.Template.Child("old_BK_W9")

    pho_BK_W1 = Gtk.Template.Child("pho_BK_W1")
    pho_BK_W2 = Gtk.Template.Child("pho_BK_W2")
    pho_BK_W3 = Gtk.Template.Child("pho_BK_W3")
    pho_BK_W4 = Gtk.Template.Child("pho_BK_W4")
    pho_BK_W5 = Gtk.Template.Child("pho_BK_W5")
    pho_BK_W6 = Gtk.Template.Child("pho_BK_W6")
    pho_BK_W7 = Gtk.Template.Child("pho_BK_W7")
    pho_BK_W8 = Gtk.Template.Child("pho_BK_W8")
    pho_BK_W9 = Gtk.Template.Child("pho_BK_W9")

    mod_BK_W1 = Gtk.Template.Child("mod_BK_W1")
    mod_BK_W2 = Gtk.Template.Child("mod_BK_W2")
    mod_BK_W3 = Gtk.Template.Child("mod_BK_W3")
    mod_BK_W4 = Gtk.Template.Child("mod_BK_W4")
    mod_BK_W5 = Gtk.Template.Child("mod_BK_W5")
    mod_BK_W6 = Gtk.Template.Child("mod_BK_W6")
    mod_BK_W7 = Gtk.Template.Child("mod_BK_W7")
    mod_BK_W8 = Gtk.Template.Child("mod_BK_W8")
    mod_BK_W9 = Gtk.Template.Child("mod_BK_W9")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
