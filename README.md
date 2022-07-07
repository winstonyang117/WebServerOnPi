# Pi Dashboard
A WebUI dashboard for raspberry pi. It also include the multiple wifi connection features. It will first try to connect the wifi with your input "name" and "password". If it fails to be connected, it will automatically use back-up wifi "sensorweb" with "snesorweb128".

Before building this dashboard, we will walk through serveral essential steps. 
Generally, this dashboard was built based on Apache and PHP7. It also includes some Javascripts and Python codes.  

### Step 1: Apahce installation
Please click [here](https://pimylifeup.com/raspberry-pi-apache/) for detailed instructions or simply follow the codes below:

```
sudo apt-get update
sudo apt-get upgrade
```
Then, install Apache2 on RPi:

```
sudo apt install apache2 -y
```

After the installation, a very basic webpage was built on our RPi. To get access to it, we should know its IP address first:
```
hostname -I
```
Go to our web browser, enter the IP address then you are able to see it. It should be noted that, if we want to make changes to the files within the /var/www/html without using root we need to setup some permissions. Firstly, we add the user pi (our user) to the www-data group, the default group for Apache2. Secondly, we give ownership to all the files and folders in the /var/www/html directory to the www-data group.
```
sudo usermod -a -G www-data pi
sudo chown -R -f www-data:www-data /var/www/html
```

You can now make changes to the default web page by running the following command.This command will use the nano text editor to modify the index.html file.
The web server will serve all files within the /var/www/html/ directory.
```
nano /var/www/html/index.html
```
### Step 2: Setting up PHP7 for Apache
Before starting this step, make sure you are **running at least Raspberry Pi OS Bullseye**, if not, you can click [here](https://pimylifeup.com/upgrade-raspberry-pi-os-bullseye/) for how to upgrade your RPi OS to RPi OS Bullseye. 

Next, we will install PHP 7.4 and several other packages to our Raspberry Pi. The additional packages we are installing are ones that are commonly used by PHP applications.
```
sudo apt install php7.4 libapache2-mod-php7.4 php7.4-mbstring php7.4-mysql php7.4-curl php7.4-gd php7.4-zip -y
```

Now that PHP7 is installed to our Raspberry Pi, we can edit "example.php" to test it.
```
sudo nano /var/www/html/example.php
```
Add the lines beblow:
```
<?php
echo "Today's date is ".date('Y-m-d H:i:s');
```
Then, control+x and Yes. Go to: http://192.168.xxx.xxx/example.php to verify if it works.

### Step 3: Clone all the files from Github
Use the command below to copy all the files under "/var/www/html". 
```
git clone https://github.com/winstonyang117/WebServerOnPi.git
```
Move all the files from **WebServerOnPi** to last path **"/var/www/html"**
```
sudo mv * ../
```
Then, you can delete the folder WebServerOnPi and index.html accordingly. 
```
sudo rm -r WebServerOnPi/
sudo rm -r index.html 
```
Then you got everything you need. Next, we should make some important changes of file ownership.

### Step 4: Ownership and permission configuration 
For Linux files, r:4 w:2 x:1 and use "chmod" to change the file's mode. Use "chown" to change the file's ownership or add user for specific file. 
1. Change mode of **"wpa_supplicant.conf"**, otherwise the wifi configuration file (configwifi.py) can't get access to it. 
```
cd /etc/wpa_supplicant
sudo chmod 777 wpa_supplicant.conf
```
2. Give ownership to www-data (include user group) for all the whole **html** folder.
```
cd /var/www/
sudo chown -R www-data:www-data html/
```
Use **"ls -al"** to check.

3. Change mode of **"configwifi.py", "index.php" and "submitWifi.php".**
```
cd /var/www/html/
sudo chmod 777 configwifi.py
sudo chmod 777 index.php
sudo chmod 777 submitWifi.php
```

**Permission for www-data to run any command:**
```
sudo nano /etc/sudoers
www-data ALL=(ALL) NOPASSWD: ALL
```

### Step 5: Make RPi IP address static (if needed)
1. To begin setting up a static IP address on our Raspberry Pi, we will first need to retrieve some information about our current network setup. Retrieve  the currently defined router for your network by running the following command.
```
ip r | grep default
```
Make a note of the first IP mentioned in this string.

2. Next, let us also retrieve the current DNS server.
```
sudo nano /etc/resolv.conf
```
Make a note of the IP next to “nameserver“. This will define the name server in our next few steps.

3. Now that we have retrieved both our current “router” IP and the nameserver IP we can proceed to modify the “dhcpcd.conf” configuration file by running the command below.
```
sudo nano /etc/dhcpcd.conf
```

4. First, you have to decide if you want to set the static IP for your “eth0” (Ethernet) connector or you “wlan0” (WiFi) connection. Decide which one you want and replace “<NETWORK>” with it.
Make sure you replace “<STATICIP>” with the IP address that you want to assign to your Raspberry Pi. Make sure this is not an IP that could be easily attached to another device on your network.
Replace “<ROUTERIP>” with the IP address that you retrieved in step 1 of this tutorial
Finally, replace “<DNSIP>” with the IP of the domain name server you want to utilize. This address is either the IP you got in step 2 or another one such as Googles “8.8.8.8” or CloudFlare’s “1.1.1.1“.
  
```
interface <NETWORK>
static ip_address=<STATICIP>/24
static routers=<ROUTERIP>
static domain_name_servers=<DNSIP>
```
Do not forget to **REBOOT** your RPi.

