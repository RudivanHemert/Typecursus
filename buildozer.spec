[app]
title = Kinder Typecursus
package.name = kindertypecursus
package.domain = org.kindertypecursus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0

requirements = python3,kivy==2.2.1,pygame

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 28
android.minapi = 21
android.sdk = 28
android.ndk = 19b
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1