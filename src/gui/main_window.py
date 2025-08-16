#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hoofdvenster voor de Kinder Typecursus
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional

from .login_screen import LoginScreen
from .dashboard import Dashboard
from .lesson_screen import LessonScreen
from .profile_screen import ProfileScreen
from .settings_screen import SettingsScreen

class MainWindow:
    """Hoofdvenster van de typecursus applicatie"""
    
    def __init__(self, root, user_manager, lesson_manager, config):
        """Initialiseer het hoofdvenster"""
        self.root = root
        self.user_manager = user_manager
        self.lesson_manager = lesson_manager
        self.config = config
        
        # Huidige scherm
        self.current_screen = None
        
        # Stel de interface in
        self.setup_interface()
        
        # Toon het loginscherm
        self.show_login_screen()
        
    def setup_interface(self):
        """Stel de basis interface in"""
        # Configureer het hoofdvenster
        self.root.configure(bg=self.config.get("colors.background", "#F5F5F5"))
        
        # Maak een hoofdframe
        self.main_frame = tk.Frame(self.root, bg=self.config.get("colors.background", "#F5F5F5"))
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Stel lettertypen in
        self.setup_fonts()
        
    def setup_fonts(self):
        """Stel de lettertypen in"""
        fonts = self.config.get_fonts()
        
        # Configureer standaard lettertypen
        default_font = fonts.get("body", ("Comic Sans MS", 14))
        self.root.option_add("*Font", default_font)
        
        # Configureer specifieke lettertypen
        style = ttk.Style()
        style.configure("Title.TLabel", font=fonts.get("title", ("Comic Sans MS", 24, "bold")))
        style.configure("Heading.TLabel", font=fonts.get("heading", ("Comic Sans MS", 18, "bold")))
        style.configure("Body.TLabel", font=fonts.get("body", ("Comic Sans MS", 14)))
        style.configure("Button.TButton", font=fonts.get("button", ("Comic Sans MS", 12, "bold")))
        
    def clear_current_screen(self):
        """Verwijder het huidige scherm"""
        if self.current_screen:
            self.current_screen.destroy()
            self.current_screen = None
            
    def show_login_screen(self):
        """Toon het loginscherm"""
        self.clear_current_screen()
        self.current_screen = LoginScreen(
            self.main_frame, 
            self.user_manager, 
            self.on_login_success
        )
        
    def show_dashboard(self):
        """Toon het dashboard"""
        self.clear_current_screen()
        self.current_screen = Dashboard(
            self.main_frame,
            self.user_manager,
            self.lesson_manager,
            self.config,
            self.on_start_lesson,
            self.on_show_profile,
            self.on_show_settings,
            self.on_logout
        )
        
    def show_lesson_screen(self, lesson_id: str):
        """Toon het lesscherm"""
        self.clear_current_screen()
        lesson = self.lesson_manager.get_lesson(lesson_id)
        if lesson:
            self.current_screen = LessonScreen(
                self.main_frame,
                lesson,
                self.user_manager,
                self.config,
                self.on_lesson_completed,
                self.on_return_to_dashboard
            )
        else:
            messagebox.showerror("Fout", "Les niet gevonden!")
            self.show_dashboard()
            
    def show_profile_screen(self):
        """Toon het profielscherm"""
        self.clear_current_screen()
        self.current_screen = ProfileScreen(
            self.main_frame,
            self.user_manager,
            self.config,
            self.on_return_to_dashboard
        )
        
    def show_settings_screen(self):
        """Toon het instellingenscherm"""
        self.clear_current_screen()
        self.current_screen = SettingsScreen(
            self.main_frame,
            self.config,
            self.on_return_to_dashboard
        )
        
    def on_login_success(self, user):
        """Callback voor succesvolle login"""
        self.user_manager.set_current_user(user)
        self.show_dashboard()
        
    def on_start_lesson(self, lesson_id: str):
        """Callback voor het starten van een les"""
        self.show_lesson_screen(lesson_id)
        
    def on_lesson_completed(self, lesson_id: str, score: int, accuracy: float, speed: float):
        """Callback voor voltooide les"""
        current_user = self.user_manager.get_current_user()
        if current_user:
            current_user.complete_lesson(lesson_id, score, accuracy, speed)
            
            # Toon resultaat
            self.show_lesson_result(lesson_id, score, accuracy, speed)
            
    def show_lesson_result(self, lesson_id: str, score: int, accuracy: float, speed: float):
        """Toon het resultaat van een voltooide les"""
        lesson = self.lesson_manager.get_lesson(lesson_id)
        
        # Maak resultaatvenster
        result_window = tk.Toplevel(self.root)
        result_window.title("Les Voltooid!")
        result_window.geometry("400x300")
        result_window.configure(bg=self.config.get("colors.background", "#F5F5F5"))
        
        # Centreren
        result_window.transient(self.root)
        result_window.grab_set()
        
        # Resultaatinhoud
        title_label = tk.Label(
            result_window,
            text="Gefeliciteerd!",
            font=self.config.get_fonts().get("title", ("Comic Sans MS", 24, "bold")),
            fg=self.config.get("colors.primary", "#4CAF50"),
            bg=self.config.get("colors.background", "#F5F5F5")
        )
        title_label.pack(pady=(20, 10))
        
        lesson_label = tk.Label(
            result_window,
            text=f"Les: {lesson.title if lesson else 'Onbekend'}",
            font=self.config.get_fonts().get("heading", ("Comic Sans MS", 18, "bold")),
            bg=self.config.get("colors.background", "#F5F5F5")
        )
        lesson_label.pack(pady=5)
        
        score_label = tk.Label(
            result_window,
            text=f"Score: {score} punten",
            font=self.config.get_fonts().get("body", ("Comic Sans MS", 14)),
            bg=self.config.get("colors.background", "#F5F5F5")
        )
        score_label.pack(pady=5)
        
        accuracy_label = tk.Label(
            result_window,
            text=f"Nauwkeurigheid: {accuracy:.1f}%",
            font=self.config.get_fonts().get("body", ("Comic Sans MS", 14)),
            bg=self.config.get("colors.background", "#F5F5F5")
        )
        accuracy_label.pack(pady=5)
        
        speed_label = tk.Label(
            result_window,
            text=f"Snelheid: {speed:.1f} WPM",
            font=self.config.get_fonts().get("body", ("Comic Sans MS", 14)),
            bg=self.config.get("colors.background", "#F5F5F5")
        )
        speed_label.pack(pady=5)
        
        # Knoppen
        button_frame = tk.Frame(result_window, bg=self.config.get("colors.background", "#F5F5F5"))
        button_frame.pack(pady=20)
        
        continue_button = tk.Button(
            button_frame,
            text="Doorgaan",
            font=self.config.get_fonts().get("button", ("Comic Sans MS", 12, "bold")),
            bg=self.config.get("colors.primary", "#4CAF50"),
            fg="white",
            command=lambda: [result_window.destroy(), self.show_dashboard()]
        )
        continue_button.pack(side=tk.LEFT, padx=10)
        
        # Auto-sluit na 5 seconden
        result_window.after(5000, lambda: [result_window.destroy(), self.show_dashboard()])
        
    def on_show_profile(self):
        """Callback voor het tonen van profiel"""
        self.show_profile_screen()
        
    def on_show_settings(self):
        """Callback voor het tonen van instellingen"""
        self.show_settings_screen()
        
    def on_return_to_dashboard(self):
        """Callback voor terugkeer naar dashboard"""
        self.show_dashboard()
        
    def on_logout(self):
        """Callback voor uitloggen"""
        self.user_manager.set_current_user(None)
        self.show_login_screen()