#!/usr/bin/python3

#Joshua Krogstad, Nov 3 2025

from geoip import geolite2
import os
import re
from datetime import datetime

# Clear terminal
os.system("clear")

# Keep track of all ips that fail a login
ip_appearances = dict()

# Check every log entry
for entry in open("/home/student/Downloads/syslog.log"):
  # Every failed login will say "Failed password"
  if "Failed password" in entry:
    # Regex for ip address
    match = re.search(r"\d{1,3}\.\d+\.\d+\.\d{1,3}", entry)
    ip_address = match.group(0)
    # If ip already exists in dict
    if ip_address in ip_appearances:
      # Increment count by 1
      ip_appearances[ip_address] += 1
    else:
      # Add ip to list at 1 appearance
      ip_appearances[ip_address] = 1

#print(ip_appearances) # DEBUG

#test_country = geolite2.lookup('8.8.8.8') # DEBUG
#print(test_country.country) # DEBUG

# Set up report title and date
to_print = "Attacker Report - " + datetime.today().strftime('%B %d, %Y') + "\n\n"

# Set up headers of list to be printed
to_print += "COUNT\tIP ADDRESS\tCOUNTRY\n"
# Sort by number of appearances
for ip_address in sorted(ip_appearances.items(), key=lambda kv: (kv[1], kv[0])):
  # If failed logins >= 10
  if (ip_address[1] >= 10):
    # Add num failed logins, source ip, and ip country to print
    to_print += str(ip_address[1]) + "\t" + str(ip_address[0]) + "\t" + geolite2.lookup(ip_address[0]).country + "\n"

# Print the chart made above
print(to_print)
