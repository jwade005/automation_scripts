#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-2051294a'
amazon_instance = 't2.micro'
amazon_pem_key = 'RedHat7-1.pem'
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
      UserData="""

      #!/usr/bin/python
      # This Python file uses the following encoding: utf-8

      import os, sys
      def my_github():
         print('Installing git.')
         os.system('sudo yum -y install git')

         print('Installing jwade005s GitHub.')
         os.system('git clone https://github.com/jwade005/install_scripts.git /home')

      my_github()

      sys.path.append('/home')

      import install_script

      install_script.install_apache()
      install_script.clone_github()
      install_script.publish_website()
      install_script.tree_install()
      install_script.django_install()
      install_script.mysite()
      install_script.mailx()
      install_script.crontab()
      install_script.dirty_cow()

"""

    )
