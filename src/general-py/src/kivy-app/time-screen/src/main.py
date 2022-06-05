#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @michalspano

# Import
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.image import Image

import datetime
from typing import Final


class MainLayout(Widget):
    def initial_button_animation(self, widget, *args):
        animate = Animation(
            opacity = 0, 
            duration = 0.25) # Animation prefs
            
        animate.start(widget)

        # Insert a fallback function upon completion of animation
        animate.bind(on_complete=self.show_main_scene)

    # Show the main scene, invoked upon fallback
    def show_main_scene(self, *args):
        # Reference static kivy objects
        img = self.ids.main_img
        text = self.ids.my_label

        text.text = f'Local time (Bratislava, Slovakia)'\
                    f'\n{current_local_time()}'

        text_animate = Animation(
            opacity = 1, 
            duration = 1)

        img_animate = Animation(
            opacity = 1, 
            size_hint = (1.5, 1.5), 
            duration = 1)

        # Start animations
        img_animate.start(img)
        text_animate.start(text)

        # Fallback to reset the screen
        text_animate.bind(on_complete=self.default_screen)


    def default_screen(self, *args):
        # Reference static kivy objects
        img = self.ids.main_img
        text = self.ids.my_label
        button = self.ids.btn
        
        # Reset to default object properties
        img_animate = Animation(
            opacity = 0, 
            size_hint = (.5, .5), 
            duration = 3.5)

        text_animate = Animation(
            opacity = 0,
            duration = 3.5)

        button_animate = Animation(
            opacity = 1,
            duration = 1)

        # Start animations
        img_animate.start(img)
        text_animate.start(text)
        button_animate.start(button)
    

class Main(App):
    def build(self):
        return MainLayout()


# Compute allocating time
def current_local_time() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')


if __name__ == '__main__':
    Main().run()
