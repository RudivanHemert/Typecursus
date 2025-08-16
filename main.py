#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactieve Typecursus voor Kinderen (8-12 jaar)
Ontwikkeld in het Nederlands
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from typing import Dict, List, Optional
import pygame

from src.gui.main_window import MainWindow
from src.data.user_manager import UserManager
from src.data.lesson_manager import LessonManager
from src.utils.config import Config

class TypingCourseApp:
    """Hoofdklasse voor de typecursus applicatie"""
    
    def __init__(self):
        """Initialiseer de typecursus applicatie"""
        self.root = tk.Tk()
        self.root.title("Kinder Typecursus - Leer Typen met Plezier!")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Initialiseer pygame voor geluid
        pygame.mixer.init()
        
        # Laad configuratie
        self.config = Config()
        
        # Initialiseer managers
        self.user_manager = UserManager()
        self.lesson_manager = LessonManager()
        
        # Stel het hoofdvenster in
        self.setup_main_window()
        
        # Stel de applicatie in voor afsluiten
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_main_window(self):
        """Stel het hoofdvenster in"""
        self.main_window = MainWindow(
            self.root, 
            self.user_manager, 
            self.lesson_manager,
            self.config
        )
        
    def run(self):
        """Start de applicatie"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Fout", f"Er is een fout opgetreden: {str(e)}")
            
    def on_closing(self):
        """Handel het afsluiten van de applicatie af"""
        try:
            # Sla alle gebruikersgegevens op
            self.user_manager.save_all_users()
            pygame.mixer.quit()
            self.root.destroy()
        except Exception as e:
            print(f"Fout bij afsluiten: {e}")
            self.root.destroy()

def main():
    """Hoofdfunctie om de applicatie te starten"""
    try:
        app = TypingCourseApp()
        app.run()
    except Exception as e:
        print(f"Kritieke fout: {e}")
        messagebox.showerror("Kritieke Fout", 
                           "De applicatie kan niet worden gestart. "
                           "Controleer of alle bestanden aanwezig zijn.")

if __name__ == "__main__":
    main()