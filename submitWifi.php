<html>
<body>

    Connected to wifi: <?php echo $_POST["ssid"]; ?><br>
    Input Username is: <?php echo $_POST["username"]; ?><br>
    Input wifi password is: <?php echo $_POST["wifi_key"]; ?><br>
    Your device will restart in 5s...
    <?php 
    $_ssid=$_POST["ssid"];
    $_key=$_POST["wifi_key"];
    $_username=$_POST["username"];
    $command = shell_exec("sudo -u www-data /usr/bin/python3 /var/www/html/configwifi.py \"$_ssid\" \"$_key\" \"$_username\"");
    $output = exec($command);
    echo $output;
    // $command = "cat $pass | su -c 'reboot'";
    // $output = array();
   
    echo shell_exec($command);
    exec($command, $output);
    system($command, $output);
    ?>
</body>
</html>



