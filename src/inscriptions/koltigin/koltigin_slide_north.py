# koltigin_slide_north.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_slide_north.ui')
class KoltiginSlideNorth(Adw.Bin):
    __gtype_name__ = 'KoltiginSlideNorth'

    old_K_N1 = Gtk.Template.Child("old_K_N1")
    old_K_N2 = Gtk.Template.Child("old_K_N2")
    old_K_N3 = Gtk.Template.Child("old_K_N3")
    old_K_N4 = Gtk.Template.Child("old_K_N4")
    old_K_N5 = Gtk.Template.Child("old_K_N5")
    old_K_N6 = Gtk.Template.Child("old_K_N6")
    old_K_N7 = Gtk.Template.Child("old_K_N7")
    old_K_N8 = Gtk.Template.Child("old_K_N8")
    old_K_N9 = Gtk.Template.Child("old_K_N9")
    old_K_N10 = Gtk.Template.Child("old_K_N10")
    old_K_N11 = Gtk.Template.Child("old_K_N11")
    old_K_N12 = Gtk.Template.Child("old_K_N12")
    old_K_N13 = Gtk.Template.Child("old_K_N13")

    pho_K_N1 = Gtk.Template.Child("pho_K_N1")
    pho_K_N2 = Gtk.Template.Child("pho_K_N2")
    pho_K_N3 = Gtk.Template.Child("pho_K_N3")
    pho_K_N4 = Gtk.Template.Child("pho_K_N4")
    pho_K_N5 = Gtk.Template.Child("pho_K_N5")
    pho_K_N6 = Gtk.Template.Child("pho_K_N6")
    pho_K_N7 = Gtk.Template.Child("pho_K_N7")
    pho_K_N8 = Gtk.Template.Child("pho_K_N8")
    pho_K_N9 = Gtk.Template.Child("pho_K_N9")
    pho_K_N10 = Gtk.Template.Child("pho_K_N10")
    pho_K_N11 = Gtk.Template.Child("pho_K_N11")
    pho_K_N12 = Gtk.Template.Child("pho_K_N12")
    pho_K_N13 = Gtk.Template.Child("pho_K_N13")

    mod_K_N1 = Gtk.Template.Child("mod_K_N1")
    mod_K_N2 = Gtk.Template.Child("mod_K_N2")
    mod_K_N3 = Gtk.Template.Child("mod_K_N3")
    mod_K_N4 = Gtk.Template.Child("mod_K_N4")
    mod_K_N5 = Gtk.Template.Child("mod_K_N5")
    mod_K_N6 = Gtk.Template.Child("mod_K_N6")
    mod_K_N7 = Gtk.Template.Child("mod_K_N7")
    mod_K_N8 = Gtk.Template.Child("mod_K_N8")
    mod_K_N9 = Gtk.Template.Child("mod_K_N9")
    mod_K_N10 = Gtk.Template.Child("mod_K_N10")
    mod_K_N11 = Gtk.Template.Child("mod_K_N11")
    mod_K_N12 = Gtk.Template.Child("mod_K_N12")
    mod_K_N13 = Gtk.Template.Child("mod_K_N13")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
