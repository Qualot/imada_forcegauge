#!/bin/sh

echo "#udev id for forcegauge
SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"1412\", ATTRS{idProduct}==\"0100\", SYMLINK+=\"forcegauge\"" > /tmp/75-forcegauge-udev.rules

sudo sh -c "cat /tmp/75-forcegauge-udev.rules > /etc/udev/rules.d/75-forcegauge-udev.rules"

sudo udevadm control --reload-rules
sudo adduser $USER dialout

echo ""
echo "forcegauge udev setup has finished."

