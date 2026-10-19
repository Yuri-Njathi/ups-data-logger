#!/bin/bash

UPS_NAME="eatonups@localhost"
LOG_FILE="/home/$(whoami)/ups_metrics_all.json"

# Fetch raw output
METRICS=$(upsc $UPS_NAME 2>/dev/null)

if [ -z "$METRICS" ]; then
    exit 1
fi

# Convert the raw "key: value" lines cleanly into a dynamic JSON object
JSON_METRICS=$(echo "$METRICS" | awk -F': ' '{gsub(/"/, "\\\"", $2); print "\""$1"\": \""$2"\""}' | paste -sd, - | sed 's/^/{/;s/$/}/')

# Add a global timestamp property to the JSON object
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
FINAL_JSON=$(echo $JSON_METRICS | jq --arg ts "$TIMESTAMP" '. + {timestamp: $ts}' -c)

# Append the line-delimited JSON entry to the log file
echo "$FINAL_JSON" >> "$LOG_FILE"
