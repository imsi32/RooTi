# koltigin_slide_northeast.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_slide_northeast.ui')
class KoltiginSlideNortheast(Adw.Bin):
    __gtype_name__ = 'KoltiginSlideNortheast'

    old_K_NE1 = Gtk.Template.Child("old_K_NE1")

    pho_K_NE1 = Gtk.Template.Child("pho_K_NE1")

    mod_K_NE1 = Gtk.Template.Child("mod_K_NE1")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
