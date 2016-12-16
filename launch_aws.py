#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-6f68cf0f'
amazon_instance = 't2.micro'
amazon_pem_key = 'RedHat7-1'
firewall_profile = ['launch-wizard-1']

print(amazon_image)
print(amazon_instance)
print(amazon_pem_key)

def launch_instance():

   instances = ec2.create_instances(
      ImageId = amazon_image,
      InstanceType = amazon_instance,
      MinCount=1,
      MaxCount=1,
      KeyName = amazon_pem_key,
      SecurityGroupIds = firewall_profile,
      UserData="""#!/usr/bin/python
      # This Python file uses the following encoding: utf-8

import os, sys, subprocess

def my_github():
    print('Installing git.')
    os.system('yum -y install git')

    print('Installing jwade005s GitHub.')
    os.system('git clone https://github.com/jwade005/install_scripts.git /python_deployment')

my_github()

sys.path.append('/python_deployment')

import install_script

def start_django():
   print('Starting the Django Web Server')
   os.system('source /opt/django/django-env/bin/python2/activate')
   os.system('source /opt/django/django-env/bin/python2/python /opt/django/mysite/mysite/manage.py runserver 0.0.0.0:8000&')

start_django()

"""

    )

   pprint.pprint(instances)


launch_instance()
