#! /bin/bash
xhost +
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority -e DISPLAY=$DISPLAY -e XAUTHORITY=/root/.Xauthority -it pycon python send_msg.py "$1" $2
xhost -