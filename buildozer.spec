[app]
title = Ink Mixer Pro
package.name = inkmixerpro
package.domain = org.inkmixer

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy==2.1.0

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

# Android configuration
[app:org.inkmixer.inkmixerpro]
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py