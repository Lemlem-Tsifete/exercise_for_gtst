#!/bin/bash

IP=$1
NSE_NAME=$2

echo "Running scan on $IP using the $NSE_NAME script..."
nmap --script $NSE_NAME $IP