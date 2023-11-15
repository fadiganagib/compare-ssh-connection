# establish-a-connection.py

# Import required modules/packages/Library
import pexpect

# Define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

#Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----FAILURE! creating session for: ', ip_address)
    exit()

# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----FAILURE! entering enable mode')
    exit()

# change the hostname to R1
session.sendline('hostname R1')
reesult = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('-------- Failure! setting hostname')


# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit

if result != 0:
   # print(password_enable)
    print('-----FAILURE! entering enable mode after sending password')
    exit()

# Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----Failure! entering config mode')
    exit()

# Check for error, if exists then display error and exit
if result != 0:
    print('----Failure! setting hostname')

# Exit config mode
session.sendline('exit')

# Exit enable mode
session.sendline('exit')

import os

OpenFile = open("example_file.txt", "w") # Open the file for writing

WriteTextToFile = OpenFile.write("establish-a-ssh-connection.py")
# Write text to the opened file

CloseTheFile = OpenFile.close() 

from difflib import Differ

# Create a Differ object
startup_config = session.sendline("show startup_config")
running_config = session.sendline("show running_config")
differ = Differ()

# Compare consequence
diff = differ.compare(startup_config.splitlines(), running_config.splitlines())

for line in diff:
    print(line)



# Exit enable mode
session.sendline('exit')

# Display a success message if works
print('------------------------------------')
print('')
print('----Success! connecting to: ', ip_address)
print('----           Username: ', username)
print('')
print('-----------------------------------------')

# Terminate SSH session
session.close()
    

# Session expecting pawwsord enter details
#session.sendline(password)
#result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
#if result != 0:
    #print('----- FAILURE! entering password: ', password)
    #exit()