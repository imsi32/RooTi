# bilge_khagan_slide_north.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/bilge_khagan/bilge_khagan_slide_north.ui')
class BilgeKhaganSlideNorth(Adw.Bin):
    __gtype_name__ = 'BilgeKhaganSlideNorth'

    old_BK_N1 = Gtk.Template.Child("old_BK_N1")
    old_BK_N2 = Gtk.Template.Child("old_BK_N2")
    old_BK_N3 = Gtk.Template.Child("old_BK_N3")
    old_BK_N4 = Gtk.Template.Child("old_BK_N4")
    old_BK_N5 = Gtk.Template.Child("old_BK_N5")
    old_BK_N6 = Gtk.Template.Child("old_BK_N6")
    old_BK_N7 = Gtk.Template.Child("old_BK_N7")
    old_BK_N8 = Gtk.Template.Child("old_BK_N8")
    old_BK_N9 = Gtk.Template.Child("old_BK_N9")
    old_BK_N10 = Gtk.Template.Child("old_BK_N10")
    old_BK_N11 = Gtk.Template.Child("old_BK_N11")
    old_BK_N12 = Gtk.Template.Child("old_BK_N12")
    old_BK_N13 = Gtk.Template.Child("old_BK_N13")
    old_BK_N14 = Gtk.Template.Child("old_BK_N14")
    old_BK_N15 = Gtk.Template.Child("old_BK_N15")

    pho_BK_N1 = Gtk.Template.Child("pho_BK_N1")
    pho_BK_N2 = Gtk.Template.Child("pho_BK_N2")
    pho_BK_N3 = Gtk.Template.Child("pho_BK_N3")
    pho_BK_N4 = Gtk.Template.Child("pho_BK_N4")
    pho_BK_N5 = Gtk.Template.Child("pho_BK_N5")
    pho_BK_N6 = Gtk.Template.Child("pho_BK_N6")
    pho_BK_N7 = Gtk.Template.Child("pho_BK_N7")
    pho_BK_N8 = Gtk.Template.Child("pho_BK_N8")
    pho_BK_N9 = Gtk.Template.Child("pho_BK_N9")
    pho_BK_N10 = Gtk.Template.Child("pho_BK_N10")
    pho_BK_N11 = Gtk.Template.Child("pho_BK_N11")
    pho_BK_N12 = Gtk.Template.Child("pho_BK_N12")
    pho_BK_N13 = Gtk.Template.Child("pho_BK_N13")
    pho_BK_N14 = Gtk.Template.Child("pho_BK_N14")
    pho_BK_N15 = Gtk.Template.Child("pho_BK_N15")

    mod_BK_N1 = Gtk.Template.Child("mod_BK_N1")
    mod_BK_N2 = Gtk.Template.Child("mod_BK_N2")
    mod_BK_N3 = Gtk.Template.Child("mod_BK_N3")
    mod_BK_N4 = Gtk.Template.Child("mod_BK_N4")
    mod_BK_N5 = Gtk.Template.Child("mod_BK_N5")
    mod_BK_N6 = Gtk.Template.Child("mod_BK_N6")
    mod_BK_N7 = Gtk.Template.Child("mod_BK_N7")
    mod_BK_N8 = Gtk.Template.Child("mod_BK_N8")
    mod_BK_N9 = Gtk.Template.Child("mod_BK_N9")
    mod_BK_N10 = Gtk.Template.Child("mod_BK_N10")
    mod_BK_N11 = Gtk.Template.Child("mod_BK_N11")
    mod_BK_N12 = Gtk.Template.Child("mod_BK_N12")
    mod_BK_N13 = Gtk.Template.Child("mod_BK_N13")
    mod_BK_N14 = Gtk.Template.Child("mod_BK_N14")
    mod_BK_N15 = Gtk.Template.Child("mod_BK_N15")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
