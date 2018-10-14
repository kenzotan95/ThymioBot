# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:12:06 2018

@author: KENZO
"""
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView
from kivy.properties import NumericProperty, BooleanProperty,\
    BoundedNumbericProperty, StringProperty, ListProperty, ObjectProperty,\
    DictProperty, AliasProperty
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import math
from kivy.garden.graph import Graph, MeshlinePlot

Builder.load_string("""
<Scn>
    Screen:
        name:"scn1"
        BoxLayout:
            cols:2
            Button:
                id:scn1_btn1
                text:"Menu"
                font_size:32
                on_press:
                    root.current="scn2"
                    root.transition.direction = 'left'
            Button:
                id:scn1_btn2
                text:"Quit"
                font_size:32
                on_press:root.on_stop()
    Screen:
        name:"scn2"
        BoxLayout
            cols:2
            Label:
                text:"Summary/Report"
                font_size:32
            Button:
                text:"Back"
                font_size:32
                on_press:
                    root.current="scn1"
                    root.transition.direction = 'right'
                    
    Screen:
        name:"scn3"
        GridLayout:
        
        
""")

class Scn(ScreenManager):
    pass

class ScnApp(App):
    def build(self):
        return Scn()
    
ScnApp().run()