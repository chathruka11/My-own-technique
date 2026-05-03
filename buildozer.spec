[app]

# (section) Title of your application
title = PusaAI

# (section) Package name
package.name = pusaai

# (section) Package domain (needed for android packaging)
package.domain = org.pusa

# (section) Source code where the main.py lives
source.dir = .

# (section) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (section) Application version (method 1)
version = 0.1

# (section) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,urllib3,certifi,chardet,idna

# (section) Supported orientations
# Valid values are: landscape, portrait, portrait-upside-down, landscape-left, landscape-right
orientation = portrait

# (section) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# (section) Kivy version to use
osx.kivy_version = 1.9.1

# (section) Python version to use
osx.python_version = 3

#
# Android specific
#

# (section) AMD64 architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (section) Allow backup
android.allow_backup = True

# (section) Minimum API your APK will support
android.minapi = 21

# (section) Android SDK version to use
android.sdk = 31

# (section) Android NDK version to use
android.ndk = 25b

# (section) Android build tools version to use
# *** මචං, මම මෙතන තමයි අර ලෙඩේ දෙන 37 වෙනුවට 33.0.0 දැම්මේ ***
android.build_tools_version = 33.0.0

# (section) Android permissions
# *** මම මෙතනට INTERNET Permission එක එකතු කළා AI එක වැඩ කරන්න ***
android.permissions = INTERNET

# (section) indicates if the application should be private or public
android.private_storage = True

[buildozer]

# (section) Log level (0 = error only, 1 = info, 2 = debug and up)
log_level = 2

# (section) Warning on root
warn_on_root = 1

