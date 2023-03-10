# koltigin_slide_southeast.py
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


@Gtk.Template(resource_path='/com/github/imsi32/RooTi/inscriptions/koltigin/koltigin_slide_southeast.ui')
class KoltiginSlideSoutheast(Adw.Bin):
    __gtype_name__ = 'KoltiginSlideSoutheast'

    old_K_SE1 = Gtk.Template.Child("old_K_SE1")

    pho_K_SE1 = Gtk.Template.Child("pho_K_SE1")

    mod_K_SE1 = Gtk.Template.Child("mod_K_SE1")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
