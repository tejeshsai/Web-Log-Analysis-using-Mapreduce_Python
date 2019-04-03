import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Frequent Websites")
        self.set_size_request(450, 150)

	vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
   	self.label = Gtk.Label()
        self.label.get_text()
	f=open("/root/hadoop-2.7.2/output/website/part-00000","r")
	vbox.pack_start(self.label, True, True, 0)
	k=f.read()
	self.label.set_text(k)
	


# after pressing "Go", grab text from entry and run num_check() with it, then set label with the result
    def on_click_me_clicked(self, button):
        number = self.entry.get_text()
	 



win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

