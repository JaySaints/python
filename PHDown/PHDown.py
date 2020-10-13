#!/usr/bin/python3

import os
import json
import time

cmd_ = os.system

# Set IP host to be checked
ip_dst = "10.41.44.66"

# Define the command execute on shell
# Status: 0 => Set the host Unreachable
# Status: 1 => Set the host Available
ping = cmd_('ping -c 4 '+ip_dst+' | grep --max-count=1 --only-matching "Unreachable" && echo {\\"status\\": 0} > resp.ping || echo {\\"status\\": 1} > resp.ping')

# Opening the file create by command above and converting the file to file.json
response = json.loads(open('resp.ping', 'rt').readline())

# Cunstom time
timestamp = time.strftime("%I:%M:%S %p", time.localtime())

if (response['status'] == 0):
    # Host Unreachable = 0
    # Create the shutdown machine log
    cmd_('echo Host shutdown at ' + timestamp + ' >> pcdown.log')
    time.sleep(1)
    # Command shutdown machine
    cmd_('systemctl reboot')
elif (response['status'] == 1):
    # Host Available = 1
    print("Host Available")
