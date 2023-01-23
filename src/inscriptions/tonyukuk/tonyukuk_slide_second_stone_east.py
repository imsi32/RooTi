# tonyukuk_slide_second_stone_east.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/tonyukuk/tonyukuk_slide_second_stone_east.ui')
class TonyukukSlideSecondStoneEast(Adw.Bin):
    __gtype_name__ = 'TonyukukSlideSecondStoneEast'

    old_T_2S_E1 = Gtk.Template.Child("old_T_2S_E1")
    old_T_2S_E2 = Gtk.Template.Child("old_T_2S_E2")
    old_T_2S_E3 = Gtk.Template.Child("old_T_2S_E3")
    old_T_2S_E4 = Gtk.Template.Child("old_T_2S_E4")
    old_T_2S_E5 = Gtk.Template.Child("old_T_2S_E5")
    old_T_2S_E6 = Gtk.Template.Child("old_T_2S_E6")
    old_T_2S_E7 = Gtk.Template.Child("old_T_2S_E7")
    old_T_2S_E8 = Gtk.Template.Child("old_T_2S_E8")

    pho_T_2S_E1 = Gtk.Template.Child("pho_T_2S_E1")
    pho_T_2S_E2 = Gtk.Template.Child("pho_T_2S_E2")
    pho_T_2S_E3 = Gtk.Template.Child("pho_T_2S_E3")
    pho_T_2S_E4 = Gtk.Template.Child("pho_T_2S_E4")
    pho_T_2S_E5 = Gtk.Template.Child("pho_T_2S_E5")
    pho_T_2S_E6 = Gtk.Template.Child("pho_T_2S_E6")
    pho_T_2S_E7 = Gtk.Template.Child("pho_T_2S_E7")
    pho_T_2S_E8 = Gtk.Template.Child("pho_T_2S_E8")

    mod_T_2S_E1 = Gtk.Template.Child("mod_T_2S_E1")
    mod_T_2S_E2 = Gtk.Template.Child("mod_T_2S_E2")
    mod_T_2S_E3 = Gtk.Template.Child("mod_T_2S_E3")
    mod_T_2S_E4 = Gtk.Template.Child("mod_T_2S_E4")
    mod_T_2S_E5 = Gtk.Template.Child("mod_T_2S_E5")
    mod_T_2S_E6 = Gtk.Template.Child("mod_T_2S_E6")
    mod_T_2S_E7 = Gtk.Template.Child("mod_T_2S_E7")
    mod_T_2S_E8 = Gtk.Template.Child("mod_T_2S_E8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
