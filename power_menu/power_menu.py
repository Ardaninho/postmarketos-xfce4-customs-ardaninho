#!/usr/bin/env python3
# Ardaninho
import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
RES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "res")

def poweroff():
    os.system("xfce4-session-logout --halt")
def reboot():
    os.system("xfce4-session-logout --reboot")
def logout():
    os.system("xfce4-session-logout --logout")
    
class PowerMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Power Menu")
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        header = Gtk.HeaderBar(title="Power Menu")
        header.set_show_close_button(False)
        cancel = Gtk.Button(label="Cancel")
        cancel.connect("clicked", lambda _b: self.destroy())
        header.pack_end(cancel)
        self.set_titlebar(header)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box.set_border_width(12)
        self.add(box)
        buttons = [
            ("Log Out", "logout.png",  logout),
            ("Restart", "restart.png",   reboot),
            ("Shut Down", "power.png", poweroff),
        ]
        for label, icon_name, action in buttons:
            btn = Gtk.Button()
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.set_border_width(6)
            image = Gtk.Image.new_from_file(os.path.join(RES_DIR, icon_name))
            vbox.pack_start(image, False, False, 0)
            vbox.pack_start(Gtk.Label(label=label), False, False, 0)
            btn.add(vbox)
            btn.connect("clicked", self._on_click, action)
            box.pack_start(btn, True, True, 0)

    def _on_click(self, _button, action):
        try:
            action()
        except Exception as e:
            dlg = Gtk.MessageDialog(
                transient_for=self, modal=True,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CLOSE, text="An error occurred",
            )
            dlg.format_secondary_text(str(e))
            dlg.run()
            dlg.destroy()
        else:
            self.destroy()

win = PowerMenu()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()