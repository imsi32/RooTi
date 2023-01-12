# tonyukuk_page.py
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

from .tonyukuk_slide_first_stone_west import TonyukukSlideFirstStoneWest
from .tonyukuk_slide_first_stone_south import TonyukukSlideFirstStoneSouth
from .tonyukuk_slide_first_stone_east import TonyukukSlideFirstStoneEast
from .tonyukuk_slide_first_stone_north import TonyukukSlideFirstStoneNorth

from .tonyukuk_slide_second_stone_west import TonyukukSlideSecondStoneWest
from .tonyukuk_slide_second_stone_south import TonyukukSlideSecondStoneSouth
from .tonyukuk_slide_second_stone_east import TonyukukSlideSecondStoneEast
from .tonyukuk_slide_second_stone_north import TonyukukSlideSecondStoneNorth


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/tonyukuk/tonyukuk_page.ui')
class PageTonyukuk(Gtk.Box):
    __gtype_name__ = 'PageTonyukuk'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
