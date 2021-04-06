from gi.repository import Gio, Gtk
import os
import gi
gi.require_version('Gtk', '3.0')


def get_thumbnail(filename, size):
    final_filename = ""
    if os.path.exists(filename):
        file = Gio.File.new_for_path(filename)
        info = file.query_info('standard::icon', 0, Gio.Cancellable())
        icon = info.get_icon().get_names()[0]

        icon_theme = Gtk.IconTheme.get_default()
        icon_file = icon_theme.lookup_icon(icon, size, 0)
        if icon_file != None:
            final_filename = icon_file.get_filename()
        return final_filename
