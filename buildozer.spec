[app]
title = PusaAI
package.name = pusaai
package.domain = org.pusa
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi,chardet,idna

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
