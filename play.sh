#!/bin/bash

result=$(pgrep -f "/usr/bin/python3 /home/dongxu/Documents/player.py")
if [[ "$result" != "" ]];then
    echo " Already Running"
else
    echo "Not Running, Lauching ... "
    # touch  /home/dongxu/Documents/test
    # /usr/bin/python3 -V >> /home/dongxu/Documents/test
    /usr/bin/python3 /home/dongxu/Documents/player.py
fi
