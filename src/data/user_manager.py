#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gebruikersmanager voor de Kinder Typecursus
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime, date

class User:
    """Klasse voor een gebruiker van de typecursus"""
    
    def __init__(self, name: str, age: int = 10):
        self.name = name
        self.age = age
        self.created_date = datetime.now().isoformat()
        self.last_login = datetime.now().isoformat()
        
        # Voortgang
        self.current_level = 1
        self.current_lesson = 1
        self.total_points = 0
        self.lessons_completed = 0
        
        # Statistieken
        self.typing_speed = 0  # woorden per minuut
        self.accuracy = 0      # percentage
        self.total_words_typed = 0
        self.total_errors = 0
        
        # Beloningen
        self.stars_earned = 0
        self.badges = []
        self.games_unlocked = []
        
        # Lesresultaten
        self.lesson_results = {}
        
    def to_dict(self) -> Dict:
        """Converteer gebruiker naar dictionary voor opslag"""
        return {
            "name": self.name,
            "age": self.age,
            "created_date": self.created_date,
            "last_login": self.last_login,
            "current_level": self.current_level,
            "current_lesson": self.current_lesson,
            "total_points": self.total_points,
            "lessons_completed": self.lessons_completed,
            "typing_speed": self.typing_speed,
            "accuracy": self.accuracy,
            "total_words_typed": self.total_words_typed,
            "total_errors": self.total_errors,
            "stars_earned": self.stars_earned,
            "badges": self.badges,
            "games_unlocked": self.games_unlocked,
            "lesson_results": self.lesson_results
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Maak gebruiker aan uit dictionary"""
        user = cls(data["name"], data["age"])
        user.created_date = data.get("created_date", user.created_date)
        user.last_login = data.get("last_login", user.last_login)
        user.current_level = data.get("current_level", 1)
        user.current_lesson = data.get("current_lesson", 1)
        user.total_points = data.get("total_points", 0)
        user.lessons_completed = data.get("lessons_completed", 0)
        user.typing_speed = data.get("typing_speed", 0)
        user.accuracy = data.get("accuracy", 0)
        user.total_words_typed = data.get("total_words_typed", 0)
        user.total_errors = data.get("total_errors", 0)
        user.stars_earned = data.get("stars_earned", 0)
        user.badges = data.get("badges", [])
        user.games_unlocked = data.get("games_unlocked", [])
        user.lesson_results = data.get("lesson_results", {})
        return user
        
    def update_login(self):
        """Update laatste login tijd"""
        self.last_login = datetime.now().isoformat()
        
    def complete_lesson(self, lesson_id: str, score: int, accuracy: float, speed: float):
        """Markeer een les als voltooid"""
        self.lesson_results[lesson_id] = {
            "completed_date": datetime.now().isoformat(),
            "score": score,
            "accuracy": accuracy,
            "speed": speed
        }
        
        self.lessons_completed += 1
        self.total_points += score
        
        # Update statistieken
        if self.lessons_completed > 0:
            self.typing_speed = (self.typing_speed + speed) / 2
            self.accuracy = (self.accuracy + accuracy) / 2
            
        # Check voor level up
        if self.lessons_completed % 5 == 0:
            self.current_level += 1
            
    def add_stars(self, count: int):
        """Voeg sterren toe"""
        self.stars_earned += count
        
    def unlock_badge(self, badge_name: str):
        """Ontgrendel een badge"""
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            
    def unlock_game(self, game_name: str):
        """Ontgrendel een minigame"""
        if game_name not in self.games_unlocked:
            self.games_unlocked.append(game_name)

class UserManager:
    """Manager voor alle gebruikers van de typecursus"""
    
    def __init__(self):
        """Initialiseer de gebruikersmanager"""
        self.users_file = "users.json"
        self.users: Dict[str, User] = {}
        self.current_user: Optional[User] = None
        
        self.load_users()
        
    def load_users(self):
        """Laad alle gebruikers uit bestand"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for user_data in data.values():
                        user = User.from_dict(user_data)
                        self.users[user.name] = user
        except Exception as e:
            print(f"Fout bij laden gebruikers: {e}")
            
    def save_all_users(self):
        """Sla alle gebruikers op in bestand"""
        try:
            data = {name: user.to_dict() for name, user in self.users.items()}
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Fout bij opslaan gebruikers: {e}")
            
    def create_user(self, name: str, age: int) -> User:
        """Maak een nieuwe gebruiker aan"""
        if name in self.users:
            raise ValueError(f"Gebruiker '{name}' bestaat al")
            
        user = User(name, age)
        self.users[name] = user
        self.save_all_users()
        return user
        
    def get_user(self, name: str) -> Optional[User]:
        """Haal een gebruiker op bij naam"""
        return self.users.get(name)
        
    def delete_user(self, name: str) -> bool:
        """Verwijder een gebruiker"""
        if name in self.users:
            del self.users[name]
            self.save_all_users()
            return True
        return False
        
    def get_all_users(self) -> List[User]:
        """Haal alle gebruikers op"""
        return list(self.users.values())
        
    def set_current_user(self, user: User):
        """Stel de huidige gebruiker in"""
        self.current_user = user
        user.update_login()
        
    def get_current_user(self) -> Optional[User]:
        """Haal de huidige gebruiker op"""
        return self.current_user
        
    def get_user_stats(self, user: User) -> Dict:
        """Haal statistieken van een gebruiker op"""
        return {
            "name": user.name,
            "age": user.age,
            "level": user.current_level,
            "lessons_completed": user.lessons_completed,
            "total_points": user.total_points,
            "typing_speed": round(user.typing_speed, 1),
            "accuracy": round(user.accuracy, 1),
            "stars_earned": user.stars_earned,
            "badges_count": len(user.badges),
            "games_unlocked": len(user.games_unlocked)
        }