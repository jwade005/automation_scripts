#!/bin/bash
for i in $( cat my_machines ); do ssh -t -i "RedHat7-1.pem" ec2-user@$i "sudo yum clean all && sudo yum update kernel && sudo reboot"; done
