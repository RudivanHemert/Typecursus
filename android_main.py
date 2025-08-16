#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android versie van de Kinder Typecursus
Gebruikt Kivy voor mobiele compatibiliteit
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import json
import os

# Voeg lettertypen toe
resource_add_path('assets/fonts')

class LoginScreen(Screen):
    """Loginscherm voor Android"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        """Stel de gebruikersinterface in"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(
            text="Kinder Typecursus 🎯",
            font_size='32sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(title)
        
        # Welkomstbericht
        welcome = Label(
            text="Leer typen met plezier!",
            font_size='18sp',
            size_hint_y=None,
            height=50
        )
        layout.add_widget(welcome)
        
        # Gebruikersnaam input
        self.username_input = TextInput(
            hint_text="Jouw naam",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.username_input)
        
        # Leeftijd input
        self.age_input = TextInput(
            hint_text="Jouw leeftijd (8-12)",
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.age_input)
        
        # Start knop
        start_button = Button(
            text="Start Typen! 🚀",
            size_hint_y=None,
            height=80,
            background_color=(0.3, 0.8, 0.3, 1)
        )
        start_button.bind(on_press=self.start_typing)
        layout.add_widget(start_button)
        
        self.add_widget(layout)
        
    def start_typing(self, instance):
        """Start de typecursus"""
        username = self.username_input.text.strip()
        try:
            age = int(self.age_input.text) if self.age_input.text else 10
        except ValueError:
            age = 10
            
        if username:
            # Ga naar het dashboard
            self.manager.current = 'dashboard'
        else:
            # Toon foutmelding
            pass

class DashboardScreen(Screen):
    """Dashboard voor Android"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        """Stel de gebruikersinterface in"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(
            text="Dashboard 📊",
            font_size='28sp',
            size_hint_y=None,
            height=80
        )
        layout.add_widget(title)
        
        # Voortgang
        progress = Label(
            text="Niveau: 1 ⭐\nLessen voltooid: 0 📚",
            font_size='16sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(progress)
        
        # Les knoppen
        lesson1_btn = Button(
            text="Les 1: De Letter A",
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.6, 0.9, 1)
        )
        lesson1_btn.bind(on_press=lambda x: self.start_lesson('L1'))
        layout.add_widget(lesson1_btn)
        
        lesson2_btn = Button(
            text="Les 2: De Letter E",
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.6, 0.9, 1)
        )
        lesson2_btn.bind(on_press=lambda x: self.start_lesson('L2'))
        layout.add_widget(lesson2_btn)
        
        # Terug knop
        back_btn = Button(
            text="← Terug naar Login",
            size_hint_y=None,
            height=50,
            background_color=(0.9, 0.3, 0.3, 1)
        )
        back_btn.bind(on_press=lambda x: self.manager.current('login'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
    def start_lesson(self, lesson_id):
        """Start een les"""
        self.manager.current = 'lesson'

class LessonScreen(Screen):
    """Lesscherm voor Android"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        """Stel de gebruikersinterface in"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(
            text="Les: De Letter A",
            font_size='24sp',
            size_hint_y=None,
            height=80
        )
        layout.add_widget(title)
        
        # Te typen tekst
        self.target_text = Label(
            text="Type deze letter: A",
            font_size='32sp',
            size_hint_y=None,
            height=100,
            color=(0.2, 0.6, 0.9, 1)
        )
        layout.add_widget(self.target_text)
        
        # Input veld
        self.typing_input = TextInput(
            hint_text="Type hier...",
            multiline=False,
            size_hint_y=None,
            height=60
        )
        self.typing_input.bind(on_text_validate=self.check_answer)
        layout.add_widget(self.typing_input)
        
        # Controleer knop
        check_btn = Button(
            text="Controleer",
            size_hint_y=None,
            height=60,
            background_color=(0.3, 0.8, 0.3, 1)
        )
        check_btn.bind(on_press=lambda x: self.check_answer())
        layout.add_widget(check_btn)
        
        # Terug knop
        back_btn = Button(
            text="← Terug naar Dashboard",
            size_hint_y=None,
            height=50,
            background_color=(0.9, 0.3, 0.3, 1)
        )
        back_btn.bind(on_press=lambda x: self.manager.current('dashboard'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
    def check_answer(self):
        """Controleer het antwoord"""
        answer = self.typing_input.text.strip()
        if answer.upper() == "A":
            # Correct antwoord
            self.target_text.text = "Gefeliciteerd! 🎉"
            self.target_text.color = (0.3, 0.8, 0.3, 1)
        else:
            # Fout antwoord
            self.target_text.text = "Probeer opnieuw!"
            self.target_text.color = (0.9, 0.3, 0.3, 1)
        
        self.typing_input.text = ""

class KinderTypecursusApp(App):
    """Hoofdapplicatie voor Android"""
    
    def build(self):
        """Bouw de applicatie"""
        # Stel schermgrootte in voor mobiel
        Window.size = (400, 600)
        
        # Maak schermmanager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(LessonScreen(name='lesson'))
        
        return sm

if __name__ == '__main__':
    KinderTypecursusApp().run()