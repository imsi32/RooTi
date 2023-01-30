# main.py
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

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import RootiWindow


class RootiApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='com.github.imsi32.RooTi',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.close, ['<primary>q'])
        self.create_action('about', self.on_about_action, ['<Ctrl>a'])
        self.create_action('preferences', self.on_preferences_action)

        self.set_accels_for_action('win.next', ['l','<Ctrl>l','<Ctrl>Right'])
        self.set_accels_for_action('win.previous', ['h','<Ctrl>h','<Ctrl>Left'])
        self.set_accels_for_action('win.up', ['k','<Ctrl>k','<Ctrl>Up'])
        self.set_accels_for_action('win.down', ['j','<Ctrl>j','<Ctrl>Down'])

        self.set_accels_for_action('win.open_bilge_khagan', ['b','<Ctrl>b'])
        self.set_accels_for_action('win.open_koltigin', ['n','<Ctrl>n'])
        self.set_accels_for_action('win.open_tonyukuk', ['m','<Ctrl>m'])

        self.set_accels_for_action('win.old', ['u','<Ctrl>u'])
        self.set_accels_for_action('win.phonologic', ['i','<Ctrl>i'])
        self.set_accels_for_action('win.modern', ['o','<Ctrl>o'])

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = RootiWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='rooti',
                                application_icon='com.github.imsi32.RooTi',
                                developer_name='imsi32',
                                version='0.1.0',
                                release_notes='<p>This version is the first minor version of the Reader Of Old Turkic Inscriptions.</p>'+
                                              '<p>In this version:</p><ul>'+
                                              '<li>User Interface Implemented</li>' +
                                              '<li>Old Scripts Added</li>'+
                                              '<li>Functionality of Buttons and Shortcuts Implemented</li>'+
                                              '<li>Metadata Implemented</li>'+
                                              '<li>Documentation Basic Template Implemented</li>'+
                                              '<li>Small Bug Fixes</li></ul>',
                                release_notes_version='0.1.0',
                                issue_url='https://github.com/imsi32/RooTi/issues',
                                developers=['imsi32'],
                                documenters=['Türk Bitig https://www.turkbitig.com/p/orhunyazitlari.html', 'imsi32'],
                                copyright='© 2022-2023 imsi32',
                                license_type="GTK_LICENSE_GPL_3_0")
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

    def close(self, *args):
        """Quit the application"""
        self.quit()


def main(version):
    """The application's entry point."""
    app = RootiApplication()
    return app.run(sys.argv)
