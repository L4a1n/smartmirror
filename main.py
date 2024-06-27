import gi
import asyncio
from weather import getWeatherToday, getWeatherWeek

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Hello GTK")
        
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        button = Gtk.Button(label="get the weather")
        button.connect("clicked", self.on_button_clicked)
        
        self.add(button)
        
    def on_button_clicked(self, widget):
        print("Button was clicked!")
        print(asyncio.run(getWeatherToday('Kassel')))
        print(asyncio.run(getWeatherWeek('Kassel')))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

