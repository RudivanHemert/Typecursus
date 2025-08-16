#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Loginscherm voor de Kinder Typecursus
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable

class LoginScreen:
    """Loginscherm voor de typecursus"""
    
    def __init__(self, parent, user_manager, on_login_success: Callable):
        self.parent = parent
        self.user_manager = user_manager
        self.on_login_success = on_login_success
        
        self.setup_ui()
        
    def setup_ui(self):
        """Stel de gebruikersinterface in"""
        # Hoofdframe
        self.frame = tk.Frame(self.parent, bg="#F5F5F5")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Titel
        title_label = tk.Label(
            self.frame,
            text="Welkom bij de Kinder Typecursus!",
            font=("Comic Sans MS", 28, "bold"),
            fg="#4CAF50",
            bg="#F5F5F5"
        )
        title_label.pack(pady=(50, 30))
        
        subtitle_label = tk.Label(
            self.frame,
            text="Leer typen met plezier! 🎉",
            font=("Comic Sans MS", 18),
            fg="#2196F3",
            bg="#F5F5F5"
        )
        subtitle_label.pack(pady=(0, 50))
        
        # Login frame
        login_frame = tk.Frame(self.frame, bg="#F5F5F5")
        login_frame.pack(pady=20)
        
        # Gebruikersnaam
        username_label = tk.Label(
            login_frame,
            text="Jouw naam:",
            font=("Comic Sans MS", 16, "bold"),
            bg="#F5F5F5"
        )
        username_label.pack(pady=10)
        
        self.username_entry = tk.Entry(
            login_frame,
            font=("Comic Sans MS", 16),
            width=20
        )
        self.username_entry.pack(pady=5)
        self.username_entry.focus()
        
        # Leeftijd
        age_label = tk.Label(
            login_frame,
            text="Jouw leeftijd:",
            font=("Comic Sans MS", 16, "bold"),
            bg="#F5F5F5"
        )
        age_label.pack(pady=10)
        
        self.age_var = tk.StringVar(value="10")
        age_spinbox = tk.Spinbox(
            login_frame,
            from_=8,
            to=12,
            textvariable=self.age_var,
            font=("Comic Sans MS", 16),
            width=10
        )
        age_spinbox.pack(pady=5)
        
        # Knoppen
        button_frame = tk.Frame(login_frame, bg="#F5F5F5")
        button_frame.pack(pady=30)
        
        login_button = tk.Button(
            button_frame,
            text="Start Typen! 🚀",
            font=("Comic Sans MS", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.login_or_create_user,
            width=15,
            height=2
        )
        login_button.pack(side=tk.LEFT, padx=10)
        
        # Bind Enter toets
        self.username_entry.bind('<Return>', lambda e: self.login_or_create_user())
        
    def login_or_create_user(self):
        """Log in of maak een nieuwe gebruiker aan"""
        username = self.username_entry.get().strip()
        try:
            age = int(self.age_var.get())
        except ValueError:
            age = 10
            
        if not username:
            messagebox.showwarning("Oeps!", "Vul je naam in!")
            return
            
        if len(username) < 2:
            messagebox.showwarning("Oeps!", "Je naam moet minstens 2 letters hebben!")
            return
            
        # Check of gebruiker bestaat
        existing_user = self.user_manager.get_user(username)
        
        if existing_user:
            # Log in met bestaande gebruiker
            self.on_login_success(existing_user)
        else:
            # Maak nieuwe gebruiker aan
            try:
                new_user = self.user_manager.create_user(username, age)
                messagebox.showinfo(
                    "Welkom!",
                    f"Hallo {username}! Je bent klaar om te leren typen! 🎯"
                )
                self.on_login_success(new_user)
            except Exception as e:
                messagebox.showerror("Fout", f"Kon geen gebruiker aanmaken: {str(e)}")