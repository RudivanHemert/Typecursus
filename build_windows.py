#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script voor Windows executable van de Kinder Typecursus
"""

import os
import subprocess
import sys
import shutil

def main():
    """Bouw de Windows executable"""
    print("🖥️  Bouwen van Windows executable...")
    
    # Controleer of PyInstaller is geïnstalleerd
    try:
        import PyInstaller
        print("✅ PyInstaller gevonden")
    except ImportError:
        print("❌ PyInstaller niet gevonden. Installeer met: pip install pyinstaller")
        return
    
    # Maak build directory
    if not os.path.exists("build"):
        os.makedirs("build")
    
    # PyInstaller commando voor Windows
    cmd = [
        "pyinstaller",
        "--onefile",                    # Eén executable bestand
        "--windowed",                   # Geen console venster
        "--name=KinderTypecursus",      # Naam van de executable
        "--add-data=src;src",           # Voeg src directory toe
        "--hidden-import=pygame",       # Voeg pygame toe
        "--hidden-import=tkinter",      # Voeg tkinter toe
        "main.py"
    ]
    
    try:
        print("🔨 Compileren...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Build succesvol!")
            print("📁 Executable bevindt zich in: dist/KinderTypecursus.exe")
            
            # Maak een installer directory
            if not os.path.exists("installer"):
                os.makedirs("installer")
            
            # Kopieer executable naar installer directory
            shutil.copy("dist/KinderTypecursus.exe", "installer/")
            
            # Maak een eenvoudige installer batch file
            create_installer_batch()
            
            print("📦 Installer bestanden gemaakt in: installer/")
            
        else:
            print("❌ Build gefaald!")
            print("Stderr:", result.stderr)
            
    except Exception as e:
        print(f"❌ Fout tijdens build: {e}")

def create_installer_batch():
    """Maak een eenvoudige installer batch file"""
    installer_content = """@echo off
echo ========================================
echo    Kinder Typecursus Installer
echo ========================================
echo.
echo Deze installer installeert de Kinder Typecursus
echo op je Windows computer.
echo.
echo Druk op een toets om te beginnen...
pause >nul

echo.
echo Installeren van Kinder Typecursus...
echo.

REM Maak programma directory
if not exist "C:\\Program Files\\KinderTypecursus" mkdir "C:\\Program Files\\KinderTypecursus"

REM Kopieer executable
copy "KinderTypecursus.exe" "C:\\Program Files\\KinderTypecursus\\"

REM Maak desktop shortcut
echo @echo off > "%USERPROFILE%\\Desktop\\Kinder Typecursus.bat"
echo "C:\\Program Files\\KinderTypecursus\\KinderTypecursus.exe" >> "%USERPROFILE%\\Desktop\\Kinder Typecursus.bat"

echo.
echo ✅ Installatie voltooid!
echo.
echo De Kinder Typecursus is geïnstalleerd in:
echo C:\\Program Files\\KinderTypecursus\\
echo.
echo Er is een snelkoppeling gemaakt op je bureaublad.
echo.
echo Druk op een toets om af te sluiten...
pause >nul
"""
    
    with open("installer/install.bat", "w", encoding="utf-8") as f:
        f.write(installer_content)

if __name__ == "__main__":
    main()