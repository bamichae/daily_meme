#! /bin/bash
# https://jmwoccassionalnotes.blog/2021/12/30/raspberry-pi-automatically-refresh-browser/#:~:text=To%20schedule%20an%20automatic%20browser,gottchas%20that%20are%20easily%20missed.&text=Note%3A%20depending%20on%20browser%20the,as%20a%20single%20long%20dash.
export XAUTHORITY=/home/pi/.Xauthority
export DISPLAY=:0
xdotool search --onlyvisible --class chromium windowfocus key F5