[app]
title = Ink Mixer Pro
package.name = inkmixerpro
package.domain = org.inkmixer

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:org.inkmixer.inkmixerpro]
# Android specific
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b