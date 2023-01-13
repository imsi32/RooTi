# bilge_khagan_page.py
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

from .bilge_khagan_slide_east import BilgeKhaganSlideEast
from .bilge_khagan_slide_southeast import BilgeKhaganSlideSoutheast
from .bilge_khagan_slide_south import BilgeKhaganSlideSouth
from .bilge_khagan_slide_north import BilgeKhaganSlideNorth
from .bilge_khagan_slide_west import BilgeKhaganSlideWest
from .bilge_khagan_slide_southwest import BilgeKhaganSlideSouthwest


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/bilge_khagan/bilge_khagan_page.ui')
class PageBilgeKhagan(Gtk.Box):
    __gtype_name__ = 'PageBilgeKhagan'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
