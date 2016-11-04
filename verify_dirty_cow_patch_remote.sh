#!/bin/bash
for i in $( cat my_machines ); do ssh -t -i "RedHat7-1.pem" ec2-user@$i "rpm -q --changelog kernel | grep CVE-2016-5195"; done
