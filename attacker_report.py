#!/usr/bin/python3

#Joshua Krogstad, Nov 3 2025

from geoip import geolite2
import os

# Clear terminal
os.system("clear")

# Keep track of all ips that fail a login
ip_appearances = dict()

# Check every log entry
for entry in open("/home/student/Downloads/syslog.log"):
  # Every failed login will say "Failed password"
  if "Failed password" in entry:
    # Regex for ip address
    match = re.search(r"\d{1,3}\.\d+\.\d+\.\d{1,3}")
    ip_address = match.group(0)
    # If ip already exists in dict
    if ip_appearances[ip_address] != None:
      # Increment count by 1
      ip_appearances[ip_address]++
    else:
      # Add ip to list at 1 appearance
      ip_appearances[ip_address] = 1

print(ip_appearances) # DEBUG
