#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuratiebestand voor de Kinder Typecursus
"""

import json
import os
from typing import Dict, Any

class Config:
    """Configuratieklasse voor de typecursus"""
    
    def __init__(self):
        """Initialiseer de configuratie"""
        self.config_file = "config.json"
        self.default_config = {
            "theme": "dieren",
            "sound_enabled": True,
            "voice_enabled": True,
            "difficulty": "beginner",
            "colors": {
                "primary": "#4CAF50",
                "secondary": "#2196F3",
                "accent": "#FF9800",
                "success": "#4CAF50",
                "error": "#F44336",
                "warning": "#FF9800",
                "background": "#F5F5F5",
                "text": "#212121"
            },
            "fonts": {
                "title": ("Comic Sans MS", 24, "bold"),
                "heading": ("Comic Sans MS", 18, "bold"),
                "body": ("Comic Sans MS", 14),
                "button": ("Comic Sans MS", 12, "bold")
            },
            "game_settings": {
                "typing_speed_target": 30,  # woorden per minuut
                "accuracy_target": 95,      # percentage
                "max_errors": 3,
                "reward_points": 10
            },
            "lessons": {
                "letters_per_lesson": 5,
                "words_per_lesson": 10,
                "sentences_per_lesson": 3
            }
        }
        
        self.config = self.load_config()
        
    def load_config(self) -> Dict[str, Any]:
        """Laad de configuratie uit bestand of gebruik standaardwaarden"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # Maak standaard configuratiebestand aan
                self.save_config(self.default_config)
                return self.default_config
        except Exception as e:
            print(f"Fout bij laden configuratie: {e}")
            return self.default_config
            
    def save_config(self, config: Dict[str, Any] = None):
        """Sla de configuratie op in bestand"""
        try:
            if config is None:
                config = self.config
                
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Fout bij opslaan configuratie: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Haal een configuratiewaarde op"""
        keys = key.split('.')
        value = self.config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
            
    def set(self, key: str, value: Any):
        """Stel een configuratiewaarde in"""
        keys = key.split('.')
        config = self.config
        
        # Navigeer naar de juiste locatie
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
            
        # Stel de waarde in
        config[keys[-1]] = value
        
        # Sla de configuratie op
        self.save_config()
        
    def get_theme_colors(self) -> Dict[str, str]:
        """Haal de kleuren voor het huidige thema op"""
        return self.get("colors", {})
        
    def get_fonts(self) -> Dict[str, tuple]:
        """Haal de lettertypen op"""
        return self.get("fonts", {})
        
    def get_game_settings(self) -> Dict[str, Any]:
        """Haal de spelinstellingen op"""
        return self.get("game_settings", {})