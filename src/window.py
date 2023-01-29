# window.py
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
from gi.repository import Gio

from .inscriptions.bilge_khagan.bilge_khagan_page import PageBilgeKhagan
from .inscriptions.koltigin.koltigin_page import PageKoltigin
from .inscriptions.tonyukuk.tonyukuk_page import PageTonyukuk


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/window.ui')
class RootiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RootiWindow'

    tb_old = Gtk.Template.Child("tb_old")
    tb_phonologic = Gtk.Template.Child("tb_phonologic")
    tb_modern = Gtk.Template.Child("tb_modern")

    scrolled_window = Gtk.Template.Child("scrolled_window")

    inscriptions_stack = Gtk.Template.Child("inscriptions_stack")

    bilge_khagan_page = Gtk.Template.Child("bilge_khagan_page")
    koltigin_page = Gtk.Template.Child("koltigin_page")
    tonyukuk_page = Gtk.Template.Child("tonyukuk_page")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        next_action = Gio.SimpleAction(name="next")
        next_action.connect("activate", self.next)
        self.add_action(next_action)

        previous_action = Gio.SimpleAction(name="previous")
        previous_action.connect("activate", self.previous)
        self.add_action(previous_action)

        up_action = Gio.SimpleAction(name="up")
        up_action.connect("activate", self.up)
        self.add_action(up_action)

        down_action = Gio.SimpleAction(name="down")
        down_action.connect("activate", self.down)
        self.add_action(down_action)

        open_bilge_khagan_action = Gio.SimpleAction(name="open_bilge_khagan")
        open_bilge_khagan_action.connect("activate", self.open_bilge_khagan)
        self.add_action(open_bilge_khagan_action)

        open_koltigin_action = Gio.SimpleAction(name="open_koltigin")
        open_koltigin_action.connect("activate", self.open_koltigin)
        self.add_action(open_koltigin_action)

        open_tonyukuk_action = Gio.SimpleAction(name="open_tonyukuk")
        open_tonyukuk_action.connect("activate", self.open_tonyukuk)
        self.add_action(open_tonyukuk_action)

        old_action= Gio.SimpleAction(name="old")
        old_action.connect("activate", self.toggle_old)
        self.add_action(old_action)

        phonologic_action= Gio.SimpleAction(name="phonologic")
        phonologic_action.connect("activate", self.toggle_phonologic)
        self.add_action(phonologic_action)

        modern_action= Gio.SimpleAction(name="modern")
        modern_action.connect("activate", self.toggle_modern)
        self.add_action(modern_action)

        self.tb_old.connect("toggled", self.visible_old)
        self.tb_phonologic.connect("toggled", self.visible_phonologic)
        self.tb_modern.connect("toggled", self.visible_modern)

        self.rows_old = [self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E1,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E2,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E3,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E4,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E5,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E6,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E7,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E8,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E9,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E10,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E11,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E12,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E13,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E14,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E15,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E16,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E17,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E18,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E19,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E20,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E21,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E22,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E23,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E24,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E25,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E26,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E27,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E28,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E29,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E30,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E31,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E32,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E33,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E34,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E35,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E36,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E38,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E39,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E40,
                         self.bilge_khagan_page.bilge_khagan_slide_east.old_BK_E41,
                         self.bilge_khagan_page.bilge_khagan_slide_southeast.old_BK_SE1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S2,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S3,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S4,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S5,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S6,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S7,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S8,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S9,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S10,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S11,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S12,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S13,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S14,
                         self.bilge_khagan_page.bilge_khagan_slide_south.old_BK_S15,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N1,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N2,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N3,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N4,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N5,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N6,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N7,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N8,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N9,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N10,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N11,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N12,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N13,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N14,
                         self.bilge_khagan_page.bilge_khagan_slide_north.old_BK_N15,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W1,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W2,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W3,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W4,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W5,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W6,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W7,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W8,
                         self.bilge_khagan_page.bilge_khagan_slide_west.old_BK_W9,
                         self.bilge_khagan_page.bilge_khagan_slide_southwest.old_BK_SW1,
                         self.koltigin_page.koltigin_slide_south.old_K_S1,
                         self.koltigin_page.koltigin_slide_south.old_K_S2,
                         self.koltigin_page.koltigin_slide_south.old_K_S3,
                         self.koltigin_page.koltigin_slide_south.old_K_S4,
                         self.koltigin_page.koltigin_slide_south.old_K_S5,
                         self.koltigin_page.koltigin_slide_south.old_K_S6,
                         self.koltigin_page.koltigin_slide_south.old_K_S7,
                         self.koltigin_page.koltigin_slide_south.old_K_S8,
                         self.koltigin_page.koltigin_slide_south.old_K_S9,
                         self.koltigin_page.koltigin_slide_south.old_K_S10,
                         self.koltigin_page.koltigin_slide_south.old_K_S11,
                         self.koltigin_page.koltigin_slide_south.old_K_S12,
                         self.koltigin_page.koltigin_slide_south.old_K_S13,
                         self.koltigin_page.koltigin_slide_east.old_K_E1,
                         self.koltigin_page.koltigin_slide_east.old_K_E2,
                         self.koltigin_page.koltigin_slide_east.old_K_E3,
                         self.koltigin_page.koltigin_slide_east.old_K_E4,
                         self.koltigin_page.koltigin_slide_east.old_K_E5,
                         self.koltigin_page.koltigin_slide_east.old_K_E6,
                         self.koltigin_page.koltigin_slide_east.old_K_E7,
                         self.koltigin_page.koltigin_slide_east.old_K_E8,
                         self.koltigin_page.koltigin_slide_east.old_K_E9,
                         self.koltigin_page.koltigin_slide_east.old_K_E10,
                         self.koltigin_page.koltigin_slide_east.old_K_E11,
                         self.koltigin_page.koltigin_slide_east.old_K_E12,
                         self.koltigin_page.koltigin_slide_east.old_K_E13,
                         self.koltigin_page.koltigin_slide_east.old_K_E14,
                         self.koltigin_page.koltigin_slide_east.old_K_E15,
                         self.koltigin_page.koltigin_slide_east.old_K_E16,
                         self.koltigin_page.koltigin_slide_east.old_K_E17,
                         self.koltigin_page.koltigin_slide_east.old_K_E18,
                         self.koltigin_page.koltigin_slide_east.old_K_E19,
                         self.koltigin_page.koltigin_slide_east.old_K_E20,
                         self.koltigin_page.koltigin_slide_east.old_K_E21,
                         self.koltigin_page.koltigin_slide_east.old_K_E22,
                         self.koltigin_page.koltigin_slide_east.old_K_E23,
                         self.koltigin_page.koltigin_slide_east.old_K_E24,
                         self.koltigin_page.koltigin_slide_east.old_K_E25,
                         self.koltigin_page.koltigin_slide_east.old_K_E26,
                         self.koltigin_page.koltigin_slide_east.old_K_E27,
                         self.koltigin_page.koltigin_slide_east.old_K_E28,
                         self.koltigin_page.koltigin_slide_east.old_K_E29,
                         self.koltigin_page.koltigin_slide_east.old_K_E30,
                         self.koltigin_page.koltigin_slide_east.old_K_E31,
                         self.koltigin_page.koltigin_slide_east.old_K_E32,
                         self.koltigin_page.koltigin_slide_east.old_K_E33,
                         self.koltigin_page.koltigin_slide_east.old_K_E34,
                         self.koltigin_page.koltigin_slide_east.old_K_E35,
                         self.koltigin_page.koltigin_slide_east.old_K_E36,
                         self.koltigin_page.koltigin_slide_east.old_K_E37,
                         self.koltigin_page.koltigin_slide_east.old_K_E38,
                         self.koltigin_page.koltigin_slide_east.old_K_E39,
                         self.koltigin_page.koltigin_slide_east.old_K_E40,
                         self.koltigin_page.koltigin_slide_north.old_K_N1,
                         self.koltigin_page.koltigin_slide_north.old_K_N2,
                         self.koltigin_page.koltigin_slide_north.old_K_N3,
                         self.koltigin_page.koltigin_slide_north.old_K_N4,
                         self.koltigin_page.koltigin_slide_north.old_K_N5,
                         self.koltigin_page.koltigin_slide_north.old_K_N6,
                         self.koltigin_page.koltigin_slide_north.old_K_N7,
                         self.koltigin_page.koltigin_slide_north.old_K_N8,
                         self.koltigin_page.koltigin_slide_north.old_K_N9,
                         self.koltigin_page.koltigin_slide_north.old_K_N10,
                         self.koltigin_page.koltigin_slide_north.old_K_N11,
                         self.koltigin_page.koltigin_slide_north.old_K_N12,
                         self.koltigin_page.koltigin_slide_north.old_K_N13,
                         self.koltigin_page.koltigin_slide_northeast.old_K_NE1,
                         self.koltigin_page.koltigin_slide_southeast.old_K_SE1,
                         self.koltigin_page.koltigin_slide_southwest.old_K_SW1,
                         self.koltigin_page.koltigin_slide_west.old_K_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.old_T_1S_W7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.old_T_1S_S10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.old_T_1S_E7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.old_T_1S_N11,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.old_T_2S_W9,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.old_T_2S_S6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.old_T_2S_E8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.old_T_2S_N1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.old_T_2S_N2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.old_T_2S_N3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.old_T_2S_N4,
                        ]

        self.rows_pho = [self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E1,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E2,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E3,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E4,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E5,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E6,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E7,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E8,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E9,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E10,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E11,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E12,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E13,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E14,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E15,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E16,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E17,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E18,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E19,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E20,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E21,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E22,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E23,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E24,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E25,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E26,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E27,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E28,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E29,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E30,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E31,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E32,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E33,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E34,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E35,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E36,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E38,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E39,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E40,
                         self.bilge_khagan_page.bilge_khagan_slide_east.pho_BK_E41,
                         self.bilge_khagan_page.bilge_khagan_slide_southeast.pho_BK_SE1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S2,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S3,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S4,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S5,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S6,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S7,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S8,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S9,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S10,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S11,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S12,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S13,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S14,
                         self.bilge_khagan_page.bilge_khagan_slide_south.pho_BK_S15,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N1,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N2,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N3,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N4,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N5,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N6,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N7,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N8,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N9,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N10,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N11,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N12,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N13,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N14,
                         self.bilge_khagan_page.bilge_khagan_slide_north.pho_BK_N15,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W1,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W2,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W3,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W4,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W5,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W6,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W7,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W8,
                         self.bilge_khagan_page.bilge_khagan_slide_west.pho_BK_W9,
                         self.bilge_khagan_page.bilge_khagan_slide_southwest.pho_BK_SW1,
                         self.koltigin_page.koltigin_slide_south.pho_K_S1,
                         self.koltigin_page.koltigin_slide_south.pho_K_S2,
                         self.koltigin_page.koltigin_slide_south.pho_K_S3,
                         self.koltigin_page.koltigin_slide_south.pho_K_S4,
                         self.koltigin_page.koltigin_slide_south.pho_K_S5,
                         self.koltigin_page.koltigin_slide_south.pho_K_S6,
                         self.koltigin_page.koltigin_slide_south.pho_K_S7,
                         self.koltigin_page.koltigin_slide_south.pho_K_S8,
                         self.koltigin_page.koltigin_slide_south.pho_K_S9,
                         self.koltigin_page.koltigin_slide_south.pho_K_S10,
                         self.koltigin_page.koltigin_slide_south.pho_K_S11,
                         self.koltigin_page.koltigin_slide_south.pho_K_S12,
                         self.koltigin_page.koltigin_slide_south.pho_K_S13,
                         self.koltigin_page.koltigin_slide_east.pho_K_E1,
                         self.koltigin_page.koltigin_slide_east.pho_K_E2,
                         self.koltigin_page.koltigin_slide_east.pho_K_E3,
                         self.koltigin_page.koltigin_slide_east.pho_K_E4,
                         self.koltigin_page.koltigin_slide_east.pho_K_E5,
                         self.koltigin_page.koltigin_slide_east.pho_K_E6,
                         self.koltigin_page.koltigin_slide_east.pho_K_E7,
                         self.koltigin_page.koltigin_slide_east.pho_K_E8,
                         self.koltigin_page.koltigin_slide_east.pho_K_E9,
                         self.koltigin_page.koltigin_slide_east.pho_K_E10,
                         self.koltigin_page.koltigin_slide_east.pho_K_E11,
                         self.koltigin_page.koltigin_slide_east.pho_K_E12,
                         self.koltigin_page.koltigin_slide_east.pho_K_E13,
                         self.koltigin_page.koltigin_slide_east.pho_K_E14,
                         self.koltigin_page.koltigin_slide_east.pho_K_E15,
                         self.koltigin_page.koltigin_slide_east.pho_K_E16,
                         self.koltigin_page.koltigin_slide_east.pho_K_E17,
                         self.koltigin_page.koltigin_slide_east.pho_K_E18,
                         self.koltigin_page.koltigin_slide_east.pho_K_E19,
                         self.koltigin_page.koltigin_slide_east.pho_K_E20,
                         self.koltigin_page.koltigin_slide_east.pho_K_E21,
                         self.koltigin_page.koltigin_slide_east.pho_K_E22,
                         self.koltigin_page.koltigin_slide_east.pho_K_E23,
                         self.koltigin_page.koltigin_slide_east.pho_K_E24,
                         self.koltigin_page.koltigin_slide_east.pho_K_E25,
                         self.koltigin_page.koltigin_slide_east.pho_K_E26,
                         self.koltigin_page.koltigin_slide_east.pho_K_E27,
                         self.koltigin_page.koltigin_slide_east.pho_K_E28,
                         self.koltigin_page.koltigin_slide_east.pho_K_E29,
                         self.koltigin_page.koltigin_slide_east.pho_K_E30,
                         self.koltigin_page.koltigin_slide_east.pho_K_E31,
                         self.koltigin_page.koltigin_slide_east.pho_K_E32,
                         self.koltigin_page.koltigin_slide_east.pho_K_E33,
                         self.koltigin_page.koltigin_slide_east.pho_K_E34,
                         self.koltigin_page.koltigin_slide_east.pho_K_E35,
                         self.koltigin_page.koltigin_slide_east.pho_K_E36,
                         self.koltigin_page.koltigin_slide_east.pho_K_E37,
                         self.koltigin_page.koltigin_slide_east.pho_K_E38,
                         self.koltigin_page.koltigin_slide_east.pho_K_E39,
                         self.koltigin_page.koltigin_slide_east.pho_K_E40,
                         self.koltigin_page.koltigin_slide_north.pho_K_N1,
                         self.koltigin_page.koltigin_slide_north.pho_K_N2,
                         self.koltigin_page.koltigin_slide_north.pho_K_N3,
                         self.koltigin_page.koltigin_slide_north.pho_K_N4,
                         self.koltigin_page.koltigin_slide_north.pho_K_N5,
                         self.koltigin_page.koltigin_slide_north.pho_K_N6,
                         self.koltigin_page.koltigin_slide_north.pho_K_N7,
                         self.koltigin_page.koltigin_slide_north.pho_K_N8,
                         self.koltigin_page.koltigin_slide_north.pho_K_N9,
                         self.koltigin_page.koltigin_slide_north.pho_K_N10,
                         self.koltigin_page.koltigin_slide_north.pho_K_N11,
                         self.koltigin_page.koltigin_slide_north.pho_K_N12,
                         self.koltigin_page.koltigin_slide_north.pho_K_N13,
                         self.koltigin_page.koltigin_slide_northeast.pho_K_NE1,
                         self.koltigin_page.koltigin_slide_southeast.pho_K_SE1,
                         self.koltigin_page.koltigin_slide_southwest.pho_K_SW1,
                         self.koltigin_page.koltigin_slide_west.pho_K_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.pho_T_1S_W7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.pho_T_1S_S10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.pho_T_1S_E7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.pho_T_1S_N11,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.pho_T_2S_W9,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.pho_T_2S_S6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.pho_T_2S_E8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.pho_T_2S_N1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.pho_T_2S_N2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.pho_T_2S_N3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.pho_T_2S_N4,
                        ]


        self.rows_mod = [self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E1,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E2,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E3,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E4,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E5,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E6,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E7,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E8,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E9,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E10,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E11,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E12,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E13,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E14,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E15,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E16,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E17,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E18,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E19,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E20,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E21,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E22,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E23,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E24,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E25,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E26,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E27,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E28,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E29,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E30,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E31,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E32,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E33,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E34,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E35,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E36,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E37,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E38,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E39,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E40,
                         self.bilge_khagan_page.bilge_khagan_slide_east.mod_BK_E41,
                         self.bilge_khagan_page.bilge_khagan_slide_southeast.mod_BK_SE1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S1,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S2,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S3,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S4,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S5,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S6,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S7,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S8,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S9,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S10,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S11,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S12,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S13,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S14,
                         self.bilge_khagan_page.bilge_khagan_slide_south.mod_BK_S15,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N1,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N2,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N3,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N4,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N5,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N6,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N7,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N8,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N9,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N10,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N11,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N12,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N13,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N14,
                         self.bilge_khagan_page.bilge_khagan_slide_north.mod_BK_N15,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W1,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W2,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W3,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W4,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W5,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W6,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W7,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W8,
                         self.bilge_khagan_page.bilge_khagan_slide_west.mod_BK_W9,
                         self.bilge_khagan_page.bilge_khagan_slide_southwest.mod_BK_SW1,
                         self.koltigin_page.koltigin_slide_south.mod_K_S1,
                         self.koltigin_page.koltigin_slide_south.mod_K_S2,
                         self.koltigin_page.koltigin_slide_south.mod_K_S3,
                         self.koltigin_page.koltigin_slide_south.mod_K_S4,
                         self.koltigin_page.koltigin_slide_south.mod_K_S5,
                         self.koltigin_page.koltigin_slide_south.mod_K_S6,
                         self.koltigin_page.koltigin_slide_south.mod_K_S7,
                         self.koltigin_page.koltigin_slide_south.mod_K_S8,
                         self.koltigin_page.koltigin_slide_south.mod_K_S9,
                         self.koltigin_page.koltigin_slide_south.mod_K_S10,
                         self.koltigin_page.koltigin_slide_south.mod_K_S11,
                         self.koltigin_page.koltigin_slide_south.mod_K_S12,
                         self.koltigin_page.koltigin_slide_south.mod_K_S13,
                         self.koltigin_page.koltigin_slide_east.mod_K_E1,
                         self.koltigin_page.koltigin_slide_east.mod_K_E2,
                         self.koltigin_page.koltigin_slide_east.mod_K_E3,
                         self.koltigin_page.koltigin_slide_east.mod_K_E4,
                         self.koltigin_page.koltigin_slide_east.mod_K_E5,
                         self.koltigin_page.koltigin_slide_east.mod_K_E6,
                         self.koltigin_page.koltigin_slide_east.mod_K_E7,
                         self.koltigin_page.koltigin_slide_east.mod_K_E8,
                         self.koltigin_page.koltigin_slide_east.mod_K_E9,
                         self.koltigin_page.koltigin_slide_east.mod_K_E10,
                         self.koltigin_page.koltigin_slide_east.mod_K_E11,
                         self.koltigin_page.koltigin_slide_east.mod_K_E12,
                         self.koltigin_page.koltigin_slide_east.mod_K_E13,
                         self.koltigin_page.koltigin_slide_east.mod_K_E14,
                         self.koltigin_page.koltigin_slide_east.mod_K_E15,
                         self.koltigin_page.koltigin_slide_east.mod_K_E16,
                         self.koltigin_page.koltigin_slide_east.mod_K_E17,
                         self.koltigin_page.koltigin_slide_east.mod_K_E18,
                         self.koltigin_page.koltigin_slide_east.mod_K_E19,
                         self.koltigin_page.koltigin_slide_east.mod_K_E20,
                         self.koltigin_page.koltigin_slide_east.mod_K_E21,
                         self.koltigin_page.koltigin_slide_east.mod_K_E22,
                         self.koltigin_page.koltigin_slide_east.mod_K_E23,
                         self.koltigin_page.koltigin_slide_east.mod_K_E24,
                         self.koltigin_page.koltigin_slide_east.mod_K_E25,
                         self.koltigin_page.koltigin_slide_east.mod_K_E26,
                         self.koltigin_page.koltigin_slide_east.mod_K_E27,
                         self.koltigin_page.koltigin_slide_east.mod_K_E28,
                         self.koltigin_page.koltigin_slide_east.mod_K_E29,
                         self.koltigin_page.koltigin_slide_east.mod_K_E30,
                         self.koltigin_page.koltigin_slide_east.mod_K_E31,
                         self.koltigin_page.koltigin_slide_east.mod_K_E32,
                         self.koltigin_page.koltigin_slide_east.mod_K_E33,
                         self.koltigin_page.koltigin_slide_east.mod_K_E34,
                         self.koltigin_page.koltigin_slide_east.mod_K_E35,
                         self.koltigin_page.koltigin_slide_east.mod_K_E36,
                         self.koltigin_page.koltigin_slide_east.mod_K_E37,
                         self.koltigin_page.koltigin_slide_east.mod_K_E38,
                         self.koltigin_page.koltigin_slide_east.mod_K_E39,
                         self.koltigin_page.koltigin_slide_east.mod_K_E40,
                         self.koltigin_page.koltigin_slide_north.mod_K_N1,
                         self.koltigin_page.koltigin_slide_north.mod_K_N2,
                         self.koltigin_page.koltigin_slide_north.mod_K_N3,
                         self.koltigin_page.koltigin_slide_north.mod_K_N4,
                         self.koltigin_page.koltigin_slide_north.mod_K_N5,
                         self.koltigin_page.koltigin_slide_north.mod_K_N6,
                         self.koltigin_page.koltigin_slide_north.mod_K_N7,
                         self.koltigin_page.koltigin_slide_north.mod_K_N8,
                         self.koltigin_page.koltigin_slide_north.mod_K_N9,
                         self.koltigin_page.koltigin_slide_north.mod_K_N10,
                         self.koltigin_page.koltigin_slide_north.mod_K_N11,
                         self.koltigin_page.koltigin_slide_north.mod_K_N12,
                         self.koltigin_page.koltigin_slide_north.mod_K_N13,
                         self.koltigin_page.koltigin_slide_northeast.mod_K_NE1,
                         self.koltigin_page.koltigin_slide_southeast.mod_K_SE1,
                         self.koltigin_page.koltigin_slide_southwest.mod_K_SW1,
                         self.koltigin_page.koltigin_slide_west.mod_K_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_west.mod_T_1S_W7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_south.mod_T_1S_S10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_east.mod_T_1S_E7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N1,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N2,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N3,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N4,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N5,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N6,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N7,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N8,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N9,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N10,
                         self.tonyukuk_page.tonyukuk_slide_first_stone_north.mod_T_1S_N11,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_west.mod_T_2S_W9,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_south.mod_T_2S_S6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E4,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E5,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E6,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E7,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_east.mod_T_2S_E8,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.mod_T_2S_N1,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.mod_T_2S_N2,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.mod_T_2S_N3,
                         self.tonyukuk_page.tonyukuk_slide_second_stone_north.mod_T_2S_N4,
                        ]

        self.tb_old.set_active(True)
        for openclose in (True, False):
            self.tb_phonologic.set_active(openclose)
            self.tb_modern.set_active(openclose)

    def toggle_old(self, *args):
        """This simple method toggle on-off tb_old for GioSimpleAction which connects tb_old with shortcuts."""
        self.tb_old.set_active(not(self.tb_old.get_active()))

    def toggle_phonologic(self, *args):
        """This simple method toggle on-off tb_phonologic for GioSimpleAction which connects tb_phonologic with shortcuts."""
        self.tb_phonologic.set_active(not(self.tb_phonologic.get_active()))

    def toggle_modern(self, *args):
        """This simple method toggle on-off tb_modern for GioSimpleAction which connects tb_modern with shortcuts."""
        self.tb_modern.set_active(not(self.tb_modern.get_active()))

    def visible_old(self, *args):
        """Sets old widgets visibility to the given button state."""
        for row_old in self.rows_old:
            row_old.set_visible(self.tb_old.get_active())

    def visible_phonologic(self, *args):
        """Sets phonologic widgets visibility to the given button state."""
        for row_pho in self.rows_pho:
            row_pho.set_visible(self.tb_phonologic.get_active())

    def visible_modern(self, button):
        """Sets modern widgets visibility to the given button state."""
        for row_mod in self.rows_mod:
            row_mod.set_visible(self.tb_modern.get_active())

    def next(self, *args):
        """Goes next carousel page of active inscription stack's carousel."""
        if self.inscriptions_stack.get_visible_child_name() == "bilge_khagan":
            carousel = self.bilge_khagan_page.bilge_khagan_carousel
        elif self.inscriptions_stack.get_visible_child_name() == "koltigin":
            carousel = self.koltigin_page.koltigin_carousel
        else:
            carousel = self.tonyukuk_page.tonyukuk_carousel

        carousel_index = carousel.get_position()
        page = carousel.get_nth_page(carousel_index + 1)
        carousel.scroll_to(page, True)

    def previous(self, *args):
        """Goes previous carousel page of active inscription stack's carousel."""
        if self.inscriptions_stack.get_visible_child_name() == "bilge_khagan":
            carousel = self.bilge_khagan_page.bilge_khagan_carousel
        elif self.inscriptions_stack.get_visible_child_name() == "koltigin":
            carousel = self.koltigin_page.koltigin_carousel
        else:
            carousel = self.tonyukuk_page.tonyukuk_carousel

        carousel_index = carousel.get_position()
        page = carousel.get_nth_page(carousel_index - 1)
        carousel.scroll_to(page, True)

    def up(self, *args):
        """Scroll the scrolled_window to up."""
        sw_vadj = self.scrolled_window.get_vadjustment()
        sw_vadj.set_value(sw_vadj.get_value() - 10)
        self.scrolled_window.set_vadjustment(sw_vadj)

    def down(self, *args):
        """Scroll the scrolled_window to down."""
        sw_vadj = self.scrolled_window.get_vadjustment()
        sw_vadj.set_value(sw_vadj.get_value() + 10)
        self.scrolled_window.set_vadjustment(sw_vadj)

    def open_bilge_khagan(self, *args):
        """Open Bilge Khagan's inscription page"""
        self.inscriptions_stack.set_visible_child_name("bilge_khagan")

    def open_koltigin(self, *args):
        """Open Koltigin's inscription page"""
        self.inscriptions_stack.set_visible_child_name("koltigin")

    def open_tonyukuk(self, *args):
        """Open Tonyukuk's inscription page"""
        self.inscriptions_stack.set_visible_child_name("tonyukuk")
