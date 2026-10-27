# Eaton ups data logging

Setup Network UPS Tools which natively supports almost all USB-based Eaton hardware using the `usbhid-ups` driver.

## Hardware setup

1. Locate the USB Type-B port on the back of your Eaton UPS (it looks like a square printer port).
2. Connect it to an open USB Type-A port on your host machine using a standard USB data cable.
3. If your host is running Linux, you can verify the connection by opening a terminal and running lsusb. You should see an entry explicitly mentioning Eaton or MGE Office Protection Systems.

## Software Configuration (Linux/Raspberry Pi)


1. Install NUT

```
sudo apt update
sudo apt install nut nut-client nut-server
```


2. Configure the UPS Driver

Open the hardware configuration file:
```
sudo nano /etc/nut/ups.conf
```
Add Eaton UPS configuration to the bottom of the file. NUT will automatically handle the USB protocols via the usbhid-ups driver:
```
[eatonups]
    driver = usbhid-ups
    port = auto
    desc = "Eaton UPS via USB"
```


3. Set the System Mode

Open the NUT daemon configuration file:
```
sudo nano /etc/nut/nut.conf
```
Set the mode to standalone since the UPS is directly attached to this single machine:
```
MODE=standalone
```


4. Start the Services

Restart NUT to apply your changes and spin up the logging drivers:
```
sudo systemctl restart nut-server nut-client
sudo upsdrvctl start
```


5. Verify Your Live Data Log

To test if data is actively pulling from your Eaton hardware, run:

`upsc eatonups@localhost`


6. Git clone this repository


This files contain python code that is used to collect Eaton UPS data 

`cd ups-data-logger`

`chmod +x log_ups.sh`

add to crontrab the comand for running the script

``` crontab -e```

command for pulling data

```* * * * * /home/<username>/log_ups.sh```

Run to view output:

```watch -n 30 "python3 ~/ups-data-logger/parse_ups_log.py | tail -20"```
