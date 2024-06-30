import gi
import asyncio
from weather import getWeatherToday

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Hello GTK")
        
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        hbox = Gtk.Box(spacing=10)
        self.add(hbox)

        button = Gtk.Button.new_with_label("get todays weather")
        button.connect("clicked", self.pressTodaysWeather)
        hbox.pack_start(button, True, True, 0)

    def pressTodaysWeather(self, widget):
        print(asyncio.run(getWeatherToday()))


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

