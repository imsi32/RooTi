# tonyukuk_slide_second_stone_north.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/tonyukuk/tonyukuk_slide_second_stone_north.ui')
class TonyukukSlideSecondStoneNorth(Adw.Bin):
    __gtype_name__ = 'TonyukukSlideSecondStoneNorth'

    old_T_2S_N1 = Gtk.Template.Child("old_T_2S_N1")
    old_T_2S_N2 = Gtk.Template.Child("old_T_2S_N2")
    old_T_2S_N3 = Gtk.Template.Child("old_T_2S_N3")
    old_T_2S_N4 = Gtk.Template.Child("old_T_2S_N4")

    pho_T_2S_N1 = Gtk.Template.Child("pho_T_2S_N1")
    pho_T_2S_N2 = Gtk.Template.Child("pho_T_2S_N2")
    pho_T_2S_N3 = Gtk.Template.Child("pho_T_2S_N3")
    pho_T_2S_N4 = Gtk.Template.Child("pho_T_2S_N4")

    mod_T_2S_N1 = Gtk.Template.Child("mod_T_2S_N1")
    mod_T_2S_N2 = Gtk.Template.Child("mod_T_2S_N2")
    mod_T_2S_N3 = Gtk.Template.Child("mod_T_2S_N3")
    mod_T_2S_N4 = Gtk.Template.Child("mod_T_2S_N4")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
