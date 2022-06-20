# Pi Dashboard
A WebUI dashboard for raspberry pi.

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

Now that PHP7 is installed to our Raspberry Pi, we can add "submitwifi.php" to it, which will pass wifi ssid and password in the future.
```
sudo nano /var/www/html/submitwifi.php
```








