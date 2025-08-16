#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesmanager voor de Kinder Typecursus
"""

import json
import os
from typing import Dict, List, Optional, Tuple
import random

class Lesson:
    """Klasse voor een typecursus les"""
    
    def __init__(self, lesson_id: str, title: str, level: int, lesson_type: str):
        self.lesson_id = lesson_id
        self.title = title
        self.level = level
        self.lesson_type = lesson_type  # 'letters', 'words', 'sentences'
        self.content = []
        self.instructions = ""
        self.target_speed = 0
        self.target_accuracy = 0
        
    def add_content(self, text: str, difficulty: int = 1):
        """Voeg inhoud toe aan de les"""
        self.content.append({
            "text": text,
            "difficulty": difficulty
        })
        
    def set_instructions(self, instructions: str):
        """Stel instructies in voor de les"""
        self.instructions = instructions
        
    def set_targets(self, speed: float, accuracy: float):
        """Stel doelen in voor snelheid en nauwkeurigheid"""
        self.target_speed = speed
        self.target_accuracy = accuracy
        
    def to_dict(self) -> Dict:
        """Converteer les naar dictionary"""
        return {
            "lesson_id": self.lesson_id,
            "title": self.title,
            "level": self.level,
            "lesson_type": self.lesson_type,
            "content": self.content,
            "instructions": self.instructions,
            "target_speed": self.target_speed,
            "target_accuracy": self.target_accuracy
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Lesson':
        """Maak les aan uit dictionary"""
        lesson = cls(
            data["lesson_id"],
            data["title"],
            data["level"],
            data["lesson_type"]
        )
        lesson.content = data.get("content", [])
        lesson.instructions = data.get("instructions", "")
        lesson.target_speed = data.get("target_speed", 0)
        lesson.target_accuracy = data.get("target_accuracy", 0)
        return lesson

class LessonManager:
    """Manager voor alle lessen van de typecursus"""
    
    def __init__(self):
        """Initialiseer de lesmanager"""
        self.lessons_file = "lessons.json"
        self.lessons: Dict[str, Lesson] = {}
        self.lesson_categories = {
            "letters": "Losse Letters",
            "words": "Woorden",
            "sentences": "Zinnen"
        }
        
        self.load_lessons()
        if not self.lessons:
            self.create_default_lessons()
            
    def load_lessons(self):
        """Laad alle lessen uit bestand"""
        try:
            if os.path.exists(self.lessons_file):
                with open(self.lessons_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for lesson_data in data.values():
                        lesson = Lesson.from_dict(lesson_data)
                        self.lessons[lesson.lesson_id] = lesson
        except Exception as e:
            print(f"Fout bij laden lessen: {e}")
            
    def save_lessons(self):
        """Sla alle lessen op in bestand"""
        try:
            data = {lid: lesson.to_dict() for lid, lesson in self.lessons.items()}
            with open(self.lessons_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Fout bij opslaan lessen: {e}")
            
    def create_default_lessons(self):
        """Maak standaard lessen aan"""
        # Niveau 1: Losse letters
        lesson1 = Lesson("L1", "De Letter A", 1, "letters")
        lesson1.set_instructions("Type de letter A zo vaak als je kunt!")
        lesson1.add_content("A", 1)
        lesson1.add_content("a", 1)
        lesson1.set_targets(5, 90)
        self.lessons["L1"] = lesson1
        
        lesson2 = Lesson("L2", "De Letter E", 1, "letters")
        lesson2.set_instructions("Type de letter E zo vaak als je kunt!")
        lesson2.add_content("E", 1)
        lesson2.add_content("e", 1)
        lesson2.set_targets(5, 90)
        self.lessons["L2"] = lesson2
        
        lesson3 = Lesson("L3", "De Letter I", 1, "letters")
        lesson3.set_instructions("Type de letter I zo vaak als je kunt!")
        lesson3.add_content("I", 1)
        lesson3.add_content("i", 1)
        lesson3.set_targets(5, 90)
        self.lessons["L3"] = lesson3
        
        # Niveau 2: Eenvoudige woorden
        lesson4 = Lesson("W1", "Eenvoudige Woorden", 2, "words")
        lesson4.set_instructions("Type deze eenvoudige woorden!")
        lesson4.add_content("kat", 1)
        lesson4.add_content("hond", 1)
        lesson4.add_content("huis", 1)
        lesson4.add_content("boom", 1)
        lesson4.add_content("zon", 1)
        lesson4.set_targets(10, 85)
        self.lessons["W1"] = lesson4
        
        lesson5 = Lesson("W2", "Dieren Woorden", 2, "words")
        lesson5.set_instructions("Type de namen van deze dieren!")
        lesson5.add_content("paard", 2)
        lesson5.add_content("koe", 1)
        lesson5.add_content("kip", 1)
        lesson5.add_content("varken", 2)
        lesson5.add_content("schaap", 2)
        lesson5.set_targets(12, 85)
        self.lessons["W2"] = lesson5
        
        # Niveau 3: Korte zinnen
        lesson6 = Lesson("Z1", "Korte Zinnen", 3, "sentences")
        lesson6.set_instructions("Type deze korte zinnen!")
        lesson6.add_content("Ik ga naar school.", 2)
        lesson6.add_content("De kat is zwart.", 2)
        lesson6.add_content("Ik hou van spelen.", 2)
        lesson6.set_targets(15, 80)
        self.lessons["Z1"] = lesson6
        
        lesson7 = Lesson("Z2", "Dierenzinnen", 3, "sentences")
        lesson7.set_instructions("Type zinnen over dieren!")
        lesson7.add_content("De hond rent in de tuin.", 3)
        lesson7.add_content("De koe geeft melk.", 2)
        lesson7.add_content("De vogel zingt mooi.", 3)
        lesson7.set_targets(18, 80)
        self.lessons["Z2"] = lesson7
        
        self.save_lessons()
        
    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        """Haal een les op bij ID"""
        return self.lessons.get(lesson_id)
        
    def get_lessons_by_level(self, level: int) -> List[Lesson]:
        """Haal alle lessen op voor een bepaald niveau"""
        return [lesson for lesson in self.lessons.values() if lesson.level == level]
        
    def get_lessons_by_type(self, lesson_type: str) -> List[Lesson]:
        """Haal alle lessen op van een bepaald type"""
        return [lesson for lesson in self.lessons.values() if lesson.lesson_type == lesson_type]
        
    def get_next_lesson(self, current_level: int, current_lesson: int) -> Optional[Lesson]:
        """Haal de volgende les op"""
        available_lessons = [l for l in self.lessons.values() 
                           if l.level == current_level and 
                           int(l.lesson_id[1:]) > current_lesson]
        
        if available_lessons:
            return min(available_lessons, key=lambda x: int(x.lesson_id[1:]))
            
        # Check voor volgende niveau
        next_level_lessons = [l for l in self.lessons.values() if l.level == current_level + 1]
        if next_level_lessons:
            return min(next_level_lessons, key=lambda x: int(x.lesson_id[1:]))
            
        return None
        
    def get_lesson_progress(self, user_level: int) -> Dict:
        """Haal voortgang van lessen op voor een gebruiker"""
        progress = {
            "current_level": user_level,
            "lessons_in_level": len(self.get_lessons_by_level(user_level)),
            "next_level": user_level + 1,
            "lessons_in_next_level": len(self.get_lessons_by_level(user_level + 1))
        }
        return progress
        
    def create_custom_lesson(self, title: str, level: int, lesson_type: str, 
                           content: List[str], instructions: str = "") -> Lesson:
        """Maak een aangepaste les aan"""
        lesson_id = f"C{len(self.lessons) + 1}"
        lesson = Lesson(lesson_id, title, level, lesson_type)
        
        for text in content:
            lesson.add_content(text, 1)
            
        lesson.set_instructions(instructions)
        lesson.set_targets(10, 85)
        
        self.lessons[lesson_id] = lesson
        self.save_lessons()
        
        return lesson
        
    def get_random_content(self, lesson_type: str, difficulty: int = 1) -> List[str]:
        """Haal willekeurige inhoud op van een bepaald type en moeilijkheidsgraad"""
        available_lessons = [l for l in self.lessons.values() 
                           if l.lesson_type == lesson_type]
        
        if not available_lessons:
            return []
            
        lesson = random.choice(available_lessons)
        content = [item["text"] for item in lesson.content 
                  if item["difficulty"] <= difficulty]
        
        return content if content else [item["text"] for item in lesson.content]