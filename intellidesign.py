
#TODO-- Importing all the widget libraries, dalle.py module and kivy module
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from dalle import *


class MyGridLayout(Widget):#TODO-- Root class
        name = ObjectProperty(None)
        update_image = ObjectProperty(None)


        def press(self):
                url = main(self.name.text)#TODO--  main function from dalle module
                self.update_image = url



class Intellidesign(App):#TODO-- Build the window
        def build(self):
                return MyGridLayout()

#TODO--program starts from here...

Intellidesign().run() 


#TODO--- Sample Prompt:

'''Create an immersive gaming room with a futuristic aesthetic.
The room should feature a large screen display, comfortable seating, and incorporate neon lighting elements. 
Use your imagination to bring this futuristic gaming room to life,
incorporating elements such as holographic displays, high-tech gaming equipment, and advanced sound systems'''
'''
a room interior design with forest theme,real,4k
'''