# koltigin_slide_east.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_slide_east.ui')
class KoltiginSlideEast(Adw.Bin):
    __gtype_name__ = 'KoltiginSlideEast'

    old_K_E1 = Gtk.Template.Child("old_K_E1")
    old_K_E2 = Gtk.Template.Child("old_K_E2")
    old_K_E3 = Gtk.Template.Child("old_K_E3")
    old_K_E4 = Gtk.Template.Child("old_K_E4")
    old_K_E5 = Gtk.Template.Child("old_K_E5")
    old_K_E6 = Gtk.Template.Child("old_K_E6")
    old_K_E7 = Gtk.Template.Child("old_K_E7")
    old_K_E8 = Gtk.Template.Child("old_K_E8")
    old_K_E9 = Gtk.Template.Child("old_K_E9")
    old_K_E10 = Gtk.Template.Child("old_K_E10")
    old_K_E11 = Gtk.Template.Child("old_K_E11")
    old_K_E12 = Gtk.Template.Child("old_K_E12")
    old_K_E13 = Gtk.Template.Child("old_K_E13")
    old_K_E14 = Gtk.Template.Child("old_K_E14")
    old_K_E15 = Gtk.Template.Child("old_K_E15")
    old_K_E16 = Gtk.Template.Child("old_K_E16")
    old_K_E17 = Gtk.Template.Child("old_K_E17")
    old_K_E18 = Gtk.Template.Child("old_K_E18")
    old_K_E19 = Gtk.Template.Child("old_K_E19")
    old_K_E20 = Gtk.Template.Child("old_K_E20")
    old_K_E21 = Gtk.Template.Child("old_K_E21")
    old_K_E22 = Gtk.Template.Child("old_K_E22")
    old_K_E23 = Gtk.Template.Child("old_K_E23")
    old_K_E24 = Gtk.Template.Child("old_K_E24")
    old_K_E25 = Gtk.Template.Child("old_K_E25")
    old_K_E26 = Gtk.Template.Child("old_K_E26")
    old_K_E27 = Gtk.Template.Child("old_K_E27")
    old_K_E28 = Gtk.Template.Child("old_K_E28")
    old_K_E29 = Gtk.Template.Child("old_K_E29")
    old_K_E30 = Gtk.Template.Child("old_K_E30")
    old_K_E31 = Gtk.Template.Child("old_K_E31")
    old_K_E32 = Gtk.Template.Child("old_K_E32")
    old_K_E33 = Gtk.Template.Child("old_K_E33")
    old_K_E34 = Gtk.Template.Child("old_K_E34")
    old_K_E35 = Gtk.Template.Child("old_K_E35")
    old_K_E36 = Gtk.Template.Child("old_K_E36")
    old_K_E37 = Gtk.Template.Child("old_K_E37")
    old_K_E38 = Gtk.Template.Child("old_K_E38")
    old_K_E39 = Gtk.Template.Child("old_K_E39")
    old_K_E40 = Gtk.Template.Child("old_K_E40")

    pho_K_E1 = Gtk.Template.Child("pho_K_E1")
    pho_K_E2 = Gtk.Template.Child("pho_K_E2")
    pho_K_E3 = Gtk.Template.Child("pho_K_E3")
    pho_K_E4 = Gtk.Template.Child("pho_K_E4")
    pho_K_E5 = Gtk.Template.Child("pho_K_E5")
    pho_K_E6 = Gtk.Template.Child("pho_K_E6")
    pho_K_E7 = Gtk.Template.Child("pho_K_E7")
    pho_K_E8 = Gtk.Template.Child("pho_K_E8")
    pho_K_E9 = Gtk.Template.Child("pho_K_E9")
    pho_K_E10 = Gtk.Template.Child("pho_K_E10")
    pho_K_E11 = Gtk.Template.Child("pho_K_E11")
    pho_K_E12 = Gtk.Template.Child("pho_K_E12")
    pho_K_E13 = Gtk.Template.Child("pho_K_E13")
    pho_K_E14 = Gtk.Template.Child("pho_K_E14")
    pho_K_E15 = Gtk.Template.Child("pho_K_E15")
    pho_K_E16 = Gtk.Template.Child("pho_K_E16")
    pho_K_E17 = Gtk.Template.Child("pho_K_E17")
    pho_K_E18 = Gtk.Template.Child("pho_K_E18")
    pho_K_E19 = Gtk.Template.Child("pho_K_E19")
    pho_K_E20 = Gtk.Template.Child("pho_K_E20")
    pho_K_E21 = Gtk.Template.Child("pho_K_E21")
    pho_K_E22 = Gtk.Template.Child("pho_K_E22")
    pho_K_E23 = Gtk.Template.Child("pho_K_E23")
    pho_K_E24 = Gtk.Template.Child("pho_K_E24")
    pho_K_E25 = Gtk.Template.Child("pho_K_E25")
    pho_K_E26 = Gtk.Template.Child("pho_K_E26")
    pho_K_E27 = Gtk.Template.Child("pho_K_E27")
    pho_K_E28 = Gtk.Template.Child("pho_K_E28")
    pho_K_E29 = Gtk.Template.Child("pho_K_E29")
    pho_K_E30 = Gtk.Template.Child("pho_K_E30")
    pho_K_E31 = Gtk.Template.Child("pho_K_E31")
    pho_K_E32 = Gtk.Template.Child("pho_K_E32")
    pho_K_E33 = Gtk.Template.Child("pho_K_E33")
    pho_K_E34 = Gtk.Template.Child("pho_K_E34")
    pho_K_E35 = Gtk.Template.Child("pho_K_E35")
    pho_K_E36 = Gtk.Template.Child("pho_K_E36")
    pho_K_E37 = Gtk.Template.Child("pho_K_E37")
    pho_K_E38 = Gtk.Template.Child("pho_K_E38")
    pho_K_E39 = Gtk.Template.Child("pho_K_E39")
    pho_K_E40 = Gtk.Template.Child("pho_K_E40")

    mod_K_E1 = Gtk.Template.Child("mod_K_E1")
    mod_K_E2 = Gtk.Template.Child("mod_K_E2")
    mod_K_E3 = Gtk.Template.Child("mod_K_E3")
    mod_K_E4 = Gtk.Template.Child("mod_K_E4")
    mod_K_E5 = Gtk.Template.Child("mod_K_E5")
    mod_K_E6 = Gtk.Template.Child("mod_K_E6")
    mod_K_E7 = Gtk.Template.Child("mod_K_E7")
    mod_K_E8 = Gtk.Template.Child("mod_K_E8")
    mod_K_E9 = Gtk.Template.Child("mod_K_E9")
    mod_K_E10 = Gtk.Template.Child("mod_K_E10")
    mod_K_E11 = Gtk.Template.Child("mod_K_E11")
    mod_K_E12 = Gtk.Template.Child("mod_K_E12")
    mod_K_E13 = Gtk.Template.Child("mod_K_E13")
    mod_K_E14 = Gtk.Template.Child("mod_K_E14")
    mod_K_E15 = Gtk.Template.Child("mod_K_E15")
    mod_K_E16 = Gtk.Template.Child("mod_K_E16")
    mod_K_E17 = Gtk.Template.Child("mod_K_E17")
    mod_K_E18 = Gtk.Template.Child("mod_K_E18")
    mod_K_E19 = Gtk.Template.Child("mod_K_E19")
    mod_K_E20 = Gtk.Template.Child("mod_K_E20")
    mod_K_E21 = Gtk.Template.Child("mod_K_E21")
    mod_K_E22 = Gtk.Template.Child("mod_K_E22")
    mod_K_E23 = Gtk.Template.Child("mod_K_E23")
    mod_K_E24 = Gtk.Template.Child("mod_K_E24")
    mod_K_E25 = Gtk.Template.Child("mod_K_E25")
    mod_K_E26 = Gtk.Template.Child("mod_K_E26")
    mod_K_E27 = Gtk.Template.Child("mod_K_E27")
    mod_K_E28 = Gtk.Template.Child("mod_K_E28")
    mod_K_E29 = Gtk.Template.Child("mod_K_E29")
    mod_K_E30 = Gtk.Template.Child("mod_K_E30")
    mod_K_E31 = Gtk.Template.Child("mod_K_E31")
    mod_K_E32 = Gtk.Template.Child("mod_K_E32")
    mod_K_E33 = Gtk.Template.Child("mod_K_E33")
    mod_K_E34 = Gtk.Template.Child("mod_K_E34")
    mod_K_E35 = Gtk.Template.Child("mod_K_E35")
    mod_K_E36 = Gtk.Template.Child("mod_K_E36")
    mod_K_E37 = Gtk.Template.Child("mod_K_E37")
    mod_K_E38 = Gtk.Template.Child("mod_K_E38")
    mod_K_E39 = Gtk.Template.Child("mod_K_E39")
    mod_K_E40 = Gtk.Template.Child("mod_K_E40")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
