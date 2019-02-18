#!/bin/bash

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' discord|grep "install ok installed")
echo Checking for library: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "dependecy not found. Setting up somelib."
  sudo apt-get --force-yes --yes install discord
else 
	python3 Main.py

fi
