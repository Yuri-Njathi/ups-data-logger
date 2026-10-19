# ups-data-logger
This files contain python code that is used to collect Eaton UPS data 



add to crontrab the comand for running the script

``` crontab -e```

command for pulling data

```* * * * * /home/<username>/log_ups.sh```

Run to view output:

```watch -n 30 "python3 ~/ups-data-logger/parse_ups_log.py | tail -20"```
