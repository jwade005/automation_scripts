#!/bin/bash
for i in $( cat my_machines ); do ssh -t -i "load-ballancer-static-content.pem" ec2-user@$i "sudo yum clean all && sudo yum update kernel && sudo reboot"; done
