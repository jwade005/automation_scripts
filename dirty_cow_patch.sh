#!/bin/bash
[ sudo yum clean all && sudo yum update kernel && sudo reboot ] || echo "OOPS! Something went wrong!"
