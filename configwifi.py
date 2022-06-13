#!/usr/bin/python
import sys
import os
import time
if len(sys.argv) >= 1:
    argv1 = sys.argv[1] # wifi ssid
    argv2 = sys.argv[2] # wifi key

def create_wpa_supplicant(ssid, wifi_key):
    
    temp_conf_file = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')

    temp_conf_file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n')
    temp_conf_file.write('update_config=1\n')
    temp_conf_file.write('\n')

    # change to a new wifi
    temp_conf_file.write('network={\n')
    temp_conf_file.write('	ssid="' + ssid + '"\n')
    if wifi_key == '':
        temp_conf_file.write('	key_mgmt=NONE\n')
    else:
        temp_conf_file.write('	psk="' + wifi_key + '"\n')
        temp_conf_file.write('	priority=2\n')
    temp_conf_file.write('	}\n\n')

    # use "sensorweb" as back up wifi
    temp_conf_file.write('network={\n')
    temp_conf_file.write('	ssid="sensorweb"\n')
    temp_conf_file.write('	psk="sensorweb128"\n')
    temp_conf_file.write('	priority=1\n')

    temp_conf_file.write('	}')
    temp_conf_file.close()
    
    time.sleep(5)

    #os.system('sudo reboot')

    # os.system('sudo mv wpa_supplicant.conf.tmp /etc/wpa_supplicant/modify_wpa_supplicant.conf')

create_wpa_supplicant(argv1, argv2)
