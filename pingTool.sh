#!/usr/bin/bash

ip=$1

echo "pingando o IP $ip"

ping -c1 $ip
