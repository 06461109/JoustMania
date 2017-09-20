#!/bin/bash

# Prevent apt from prompting us about restarting services.
export DEBIAN_FRONTEND=noninteractive

#update OS
sudo cp -v conf/sources.list /etc/apt/sources.list || exit -1
sudo cp -v conf/apt.conf /etc/apt/apt.conf.d/10joustmania-conf || exit -1
sudo apt-get update -y
sudo apt-get dist-upgrade -y
cd /home/pi

#TODO: remove pyaudio and dependencies
#install components
sudo apt-get install -y  \
    python3.6 python3.6-dev python3-pip \
    python3-pkg-resources python3-setuptools libdpkg-perl \
    libsdl1.2-dev libsdl-mixer1.2-dev libsdl-sound1.2-dev \
    libportmidi-dev \
    libsdl-image1.2-dev libsdl-ttf2.0-dev \
    bluez python3-pyaudio \
    supervisor \
    cmake \
    libudev-dev swig libbluetooth-dev \
    alsa-utils alsa-tools libasound2-dev || exit -1

sudo apt-get install -y -t buster libasound2-dev libasound2 python3-numpy python3-scipy
sudo python3.6 -m pip install --upgrade virtualenv || exit -1
sudo python3.6 -m pip install psutil flask Flask-WTF pyalsaaudio pydub pygame || exit -1

#install components for psmoveapi
sudo apt-get install -y \
    build-essential \
    libv4l-dev libopencv-dev \
    libudev-dev libbluetooth-dev \
    python3-dev swig3.0 || exit -1

#install psmoveapi
git clone --recursive git://github.com/thp/psmoveapi.git
cd psmoveapi

mkdir build
cd build
# we definitely don't need java, opengj, csharp, etc
cmake .. \
    -DPSMOVE_BUILD_CSHARP_BINDINGS:BOOL=OFF \
    -DPSMOVE_BUILD_EXAMPLES:BOOL=OFF \
    -DPSMOVE_BUILD_JAVA_BINDINGS:BOOL=OFF \
    -DPSMOVE_BUILD_OPENGL_EXAMPLES:BOOL=OFF \
    -DPSMOVE_BUILD_PROCESSING_BINDINGS:BOOL=OFF \
    -DPSMOVE_BUILD_TESTS:BOOL=OFF \
    -DPSMOVE_BUILD_TRACKER:BOOL=ON \
    -DPSMOVE_USE_PSEYE:BOOL=OFF
make -j4

#installs custom supervisor script for running joustmania on startup
sudo cp -r /home/pi/JoustMania/conf/supervisor/ /etc/

#sound card is not required anymore TODO: eventually delete
#makes sound card 1(usb audio) to be default output
#use aplay -l to check sound card number
#sudo cp /home/pi/JoustMania/asound.conf /etc/


#allows python path to be kept after sudo command
OLD='env_reset'
NEW='env_keep += "PYTHONPATH"'
sudo sed -i -e "s/$OLD/$NEW/g" /etc/sudoers

sudo reboot
