# 🚀 Bouwinstructies voor Kinder Typecursus

Deze instructies leggen uit hoe je de Kinder Typecursus kunt bouwen voor verschillende platforms.

## 📱 Android APK Bouwen

### Vereisten
- **Python 3.8+**
- **Linux of WSL (Windows Subsystem for Linux)**
- **Java JDK 8**
- **Android SDK**

### Stap 1: Installeer dependencies
```bash
pip install -r requirements_android.txt
```

### Stap 2: Installeer Buildozer
```bash
pip install buildozer
```

### Stap 3: Initialiseer Buildozer (alleen eerste keer)
```bash
buildozer init
```

### Stap 4: Bouw de APK
```bash
buildozer android debug
```

### Stap 5: Installeer op je telefoon
```bash
buildozer android debug deploy
```

**Resultaat**: `bin/kindertypecursus-1.0-debug.apk`

---

## 🖥️ Windows Executable Bouwen

### Vereisten
- **Python 3.8+**
- **Windows 10/11**

### Stap 1: Installeer dependencies
```bash
pip install -r requirements.txt
```

### Stap 2: Bouw de executable
```bash
python build_windows.py
```

### Stap 3: Vind de bestanden
- **Executable**: `dist/KinderTypecursus.exe`
- **Installer**: `installer/install.bat`

---

## 🐧 Linux Executable Bouwen

### Vereisten
- **Python 3.8+**
- **Linux (Ubuntu/Debian)**

### Stap 1: Installeer dependencies
```bash
pip install -r requirements.txt
```

### Stap 2: Bouw de executable
```bash
pyinstaller --onefile --windowed --name=KinderTypecursus main.py
```

---

## 📋 Troubleshooting

### Android APK Problemen

**Probleem**: Buildozer kan geen APK bouwen
**Oplossing**: 
```bash
# Verwijder buildozer cache
buildozer android clean

# Probeer opnieuw
buildozer android debug
```

**Probleem**: Java JDK niet gevonden
**Oplossing**:
```bash
# Installeer OpenJDK
sudo apt-get install openjdk-8-jdk

# Stel JAVA_HOME in
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

### Windows Executable Problemen

**Probleem**: PyInstaller kan niet starten
**Oplossing**:
```bash
# Herinstalleer PyInstaller
pip uninstall pyinstaller
pip install pyinstaller==6.1.0
```

**Probleem**: Executable crasht bij start
**Oplossing**:
```bash
# Bouw met console voor debugging
pyinstaller --onefile --name=KinderTypecursus main.py
```

---

## 🔧 Aanpassingen

### APK Aanpassingen
Bewerk `buildozer.spec`:
- **App naam**: `title = Jouw App Naam`
- **Package naam**: `package.name = jouwappnaam`
- **Versie**: `version = 1.1`

### Windows Executable Aanpassingen
Bewerk `build_windows.py`:
- **Executable naam**: `--name=JouwAppNaam`
- **Icon toevoegen**: `--icon=icon.ico`

---

## 📱 APK Installeren op Android

1. **Schakel "Onbekende bronnen" in** in Android instellingen
2. **Kopieer de APK** naar je telefoon
3. **Open de APK** en volg de installatie-instructies
4. **Start de app** en geniet van de typecursus!

---

## 🖥️ Windows Installer Gebruiken

1. **Download** alle bestanden uit de `installer/` map
2. **Dubbelklik** op `install.bat`
3. **Volg** de installatie-instructies
4. **Start** de typecursus vanaf je bureaublad!

---

## 🎯 Snelle Start

### Voor Android (Linux/WSL):
```bash
pip install buildozer
buildozer android debug
```

### Voor Windows:
```bash
pip install pyinstaller
python build_windows.py
```

### Voor Linux:
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

---

## 📞 Ondersteuning

Als je problemen ondervindt:
1. **Controleer** alle vereisten
2. **Lees** de foutmeldingen zorgvuldig
3. **Probeer** de troubleshooting stappen
4. **Raadpleeg** de officiële documentatie van de tools

Veel succes met het bouwen van je Kinder Typecursus! 🎉