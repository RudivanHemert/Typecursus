#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test bestand voor de Android versie van de Kinder Typecursus
"""

def test_android_imports():
    """Test of alle benodigde modules kunnen worden geïmporteerd"""
    try:
        print("🧪 Testen van Android dependencies...")
        
        # Test Kivy
        try:
            import kivy
            print("✅ Kivy geïmporteerd:", kivy.__version__)
        except ImportError:
            print("❌ Kivy niet gevonden. Installeer met: pip install kivy")
            
        # Test KivyMD
        try:
            import kivymd
            print("✅ KivyMD geïmporteerd")
        except ImportError:
            print("❌ KivyMD niet gevonden. Installeer met: pip install kivymd")
            
        # Test Buildozer
        try:
            import buildozer
            print("✅ Buildozer geïmporteerd")
        except ImportError:
            print("❌ Buildozer niet gevonden. Installeer met: pip install buildozer")
            
        print("\n🎯 Android test voltooid!")
        
    except Exception as e:
        print(f"❌ Fout tijdens testen: {e}")

if __name__ == "__main__":
    test_android_imports()