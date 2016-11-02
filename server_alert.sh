#!/bin/bash

echo -e "Server Alert: `hostname`:\n `uptime -p` \n USERS: `who` " | mail -s "Server Alert! `hostname`" wadejs@icloud.com
