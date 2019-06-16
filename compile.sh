#!/bin/bash
pyinstaller --onefile SystemManagement.spec

sudo cp dist/SystemManagement /usr/bin/

sudo cp SystemManagement.service /lib/systemd/system/SystemManagement.service

sudo systemctl daemon-reload
sudo systemctl enable SystemManagement.service
sudo systemctl start SystemManagement.service
