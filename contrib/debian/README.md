
Debian
====================
This directory contains files used to package collegicoind/collegicoin-qt
for Debian-based Linux systems. If you compile collegicoind/collegicoin-qt yourself, there are some useful files here.

## collegicoin: URI support ##


collegicoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install collegicoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your collegicoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/collegicoin128.png` to `/usr/share/pixmaps`

collegicoin-qt.protocol (KDE)

