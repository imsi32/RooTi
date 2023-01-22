# koltigin_page.py
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

from .koltigin_slide_south import KoltiginSlideSouth
from .koltigin_slide_east import KoltiginSlideEast
from .koltigin_slide_north import KoltiginSlideNorth
from .koltigin_slide_northeast import KoltiginSlideNortheast
from .koltigin_slide_southeast import KoltiginSlideSoutheast
from .koltigin_slide_southwest import KoltiginSlideSouthwest
from .koltigin_slide_west import KoltiginSlideWest


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_page.ui')
class PageKoltigin(Gtk.Box):
    __gtype_name__ = 'PageKoltigin'

    koltigin_slide_south = Gtk.Template.Child("koltigin_slide_south")
    koltigin_slide_east = Gtk.Template.Child("koltigin_slide_east")
    koltigin_slide_north = Gtk.Template.Child("koltigin_slide_north")
    koltigin_slide_northeast = Gtk.Template.Child("koltigin_slide_northeast")
    koltigin_slide_southeast = Gtk.Template.Child("koltigin_slide_southeast")
    koltigin_slide_southwest = Gtk.Template.Child("koltigin_slide_southwest")
    koltigin_slide_west = Gtk.Template.Child("koltigin_slide_west")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
