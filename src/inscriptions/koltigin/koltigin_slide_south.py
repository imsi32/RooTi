# koltigin_slide_south.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_slide_south.ui')
class KoltiginSlideSouth(Adw.Bin):
    __gtype_name__ = 'KoltiginSlideSouth'

    old_K_S1 = Gtk.Template.Child("old_K_S1")
    old_K_S2 = Gtk.Template.Child("old_K_S2")
    old_K_S3 = Gtk.Template.Child("old_K_S3")
    old_K_S4 = Gtk.Template.Child("old_K_S4")
    old_K_S5 = Gtk.Template.Child("old_K_S5")
    old_K_S6 = Gtk.Template.Child("old_K_S6")
    old_K_S7 = Gtk.Template.Child("old_K_S7")
    old_K_S8 = Gtk.Template.Child("old_K_S8")
    old_K_S9 = Gtk.Template.Child("old_K_S9")
    old_K_S10 = Gtk.Template.Child("old_K_S10")
    old_K_S11 = Gtk.Template.Child("old_K_S11")
    old_K_S12 = Gtk.Template.Child("old_K_S12")
    old_K_S13 = Gtk.Template.Child("old_K_S13")

    pho_K_S1 = Gtk.Template.Child("pho_K_S1")
    pho_K_S2 = Gtk.Template.Child("pho_K_S2")
    pho_K_S3 = Gtk.Template.Child("pho_K_S3")
    pho_K_S4 = Gtk.Template.Child("pho_K_S4")
    pho_K_S5 = Gtk.Template.Child("pho_K_S5")
    pho_K_S6 = Gtk.Template.Child("pho_K_S6")
    pho_K_S7 = Gtk.Template.Child("pho_K_S7")
    pho_K_S8 = Gtk.Template.Child("pho_K_S8")
    pho_K_S9 = Gtk.Template.Child("pho_K_S9")
    pho_K_S10 = Gtk.Template.Child("pho_K_S10")
    pho_K_S11 = Gtk.Template.Child("pho_K_S11")
    pho_K_S12 = Gtk.Template.Child("pho_K_S12")
    pho_K_S13 = Gtk.Template.Child("pho_K_S13")

    mod_K_S1 = Gtk.Template.Child("mod_K_S1")
    mod_K_S2 = Gtk.Template.Child("mod_K_S2")
    mod_K_S3 = Gtk.Template.Child("mod_K_S3")
    mod_K_S4 = Gtk.Template.Child("mod_K_S4")
    mod_K_S5 = Gtk.Template.Child("mod_K_S5")
    mod_K_S6 = Gtk.Template.Child("mod_K_S6")
    mod_K_S7 = Gtk.Template.Child("mod_K_S7")
    mod_K_S8 = Gtk.Template.Child("mod_K_S8")
    mod_K_S9 = Gtk.Template.Child("mod_K_S9")
    mod_K_S10 = Gtk.Template.Child("mod_K_S10")
    mod_K_S11 = Gtk.Template.Child("mod_K_S11")
    mod_K_S12 = Gtk.Template.Child("mod_K_S12")
    mod_K_S13 = Gtk.Template.Child("mod_K_S13")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
