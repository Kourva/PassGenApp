#!/usr/bin/env python3

## Password Generator App Made With KivyMD
## GITHUB: https://github.com/Izolabela

# Imports
from sys import exit
from random import choices
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.toolbar.toolbar import MDTopAppBar, MDBottomAppBar
from kivymd.uix.textfield import MDTextField, MDTextFieldRect

# App Class
class PassGenApp(MDApp):
    # Password Generator
    def generate(self, *args):
        words = "9ab#cXd8efgh$7ijk@R1m6no!pqVWrs5tuvTUYw0xyz4ABCDEFGH3IJKLMNl2QO&PSZ"
        self.Output.text = "".join(choices(words, k=20))
    
    # Clears OutPut
    def clear(self, *args):
        self.Output.text = ""
 
    # Opens Github Dialog
    def githubOpen(self, *args):
        self.Github.open()

    # Closes Github Dialog
    def githubClose(self, *args):
        self.Github.dismiss(force=True)

    # Love You
    def loveYou(self, *args):
        self.Output.text = "Love You <3"

    # Build
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"

        home = MDScreen()

        # Top Toolbar
        self.Toolbar = MDTopAppBar(
            opposite_colors = True,
            title = "PassGenApp",
            right_action_items = [
                ["heart", self.loveYou],
                ["github", self.githubOpen],
                ["close-thick", lambda _: exit()]
            ]
        ) 

        # OutPut
        self.Output = MDTextFieldRect(
            cursor_blink = True,
            font_size = 20,
            use_handles = True,
            halign = "center",
            size_hint = (0.5, None),
            multiline = False,
            height = "40dp",
            pos_hint = {"center_x": 0.5, "center_y": 0.6},
            background_color = "#aaaaaa",        )

        # Generate Botton
        self.GBotton = MDRaisedButton(
            text = "Generate",
            text_color = "black",
            line_color = "black",
            size_hint = (0.2, None),
            height = "30dp",
            pos_hint = {"center_x": 0.35, "center_y": 0.5},
            on_press = self.generate
        )

        # Clear Botton
        self.CBotton = MDRaisedButton(
            text = "Clear",
            text_color = "black",
            line_color = "black",
            size_hint = (0.2, None),
            height = "30dp",
            pos_hint = {"center_x": 0.65, "center_y": 0.5},
            on_press = self.clear
        )

        # Text Label
        self.Text = MDLabel(
            text = "Easy To Use GUI Password Generator App",
            font_style = "H6",
            halign = "center",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
        )

        # Github Dialog
        self.Github = MDDialog(
            title = "Developer",
            text = "Support me by giving a star :D\n\nhttps://github.com/Izolabela/PassGenApp",
            buttons = [
                MDFlatButton(
                    text = "Close",
                    theme_text_color = "Custom",
                    text_color = "#aaaaaa",
                    on_press = self.githubClose
                )
            ]
        )

        # Add Widgets and Items
        home.add_widget(self.Toolbar)
        home.add_widget(self.Output)
        home.add_widget(self.GBotton)
        home.add_widget(self.CBotton)
        home.add_widget(self.Text)

        # Return Home 
        return home

# Run
PassGenApp().run()
