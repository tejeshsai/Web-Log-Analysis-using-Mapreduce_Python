import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Peak Hours")
        self.set_size_request(450, 150)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.get_text()
        self.entry.connect("activate", self.on_entry_activate)
        vbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button.new_with_label("Go")
        button.connect("clicked", self.on_click_me_clicked)
        vbox.pack_start(button, True, True, 0)

        self.label = Gtk.Label()
        self.label.get_text()
        vbox.pack_start(self.label, True, True, 0)
	self.label.set_text("Enter the number of peakhours for the traffic")

    def on_entry_activate (self, entry):
        number = entry.get_text()



    def on_click_me_clicked(self, button):
        number = self.entry.get_text()
	f=open("/root/hadoop-2.7.2/reducer1.py","r")
	print(f.read()+number+")")
	 



win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

