#!/bin/bash

var=$(cat /proc/uptime | cut -d " " -f1)
users=$(/usr/bin/who | grep -c "")

if [ "$var" > "720" ]; then
    echo "Server `hostname` has been up for more than 2 hours!"
    echo "Number of users logged on: $users"
fi
        if [ "$users" -ge "1" ]; then
            echo "There are users logged on."

        else
            echo "There are no users logged on."
fi
