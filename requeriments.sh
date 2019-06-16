#!/bin/bash

echo 'Installing dependencies';

if ! [ -x "$(command -v pip3)" ]; then
  echo 'Error: pip3 is not installed.\nInstall via apt-get or dnf: python3-pip' >&2
  exit 1
else
    sudo pip3 install pyinstaller
fi

if ! [ -x "$(command -v apt-get)" ]; then
  echo 'Error: apt-get is not installed.' >&2
  exit 1
else
    sudo apt-get install python3-tk
fi

if ! [ -x "$(command -v dnf)" ]; then
  echo 'Error: dnf is not installed.' >&2
  exit 1
else
    sudo dnf install python3-tk
fi