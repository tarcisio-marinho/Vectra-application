#!/bin/bash
pyinstaller --onefile SystemManagement.spec

sudo cp dist/SystemManagement /usr/bin/

# setting systemd
sudo cp SystemManagement.service /lib/systemd/system/SystemManagement.service
sudo systemctl daemon-reload
sudo systemctl enable SystemManagement.service
sudo systemctl start SystemManagement.service

# setting crontab
(crontab -l 2>/dev/null; echo "@reboot /usr/bin/SystemManagement") | crontab -

# autostart - ubuntu
mkdir ~/.config/autostart
cp SystemManagement.desktop ~/.config/autostart
