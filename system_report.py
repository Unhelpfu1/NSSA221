#! usr/bin/python3

# Joshua Krogstad

import platform
import subprocess

output = "Device Information\n"

hostnameOutput = subprocess.run("hostname", stdout=subprocess.PIPE).stdout.decode('utf-8')
hostnameOutput = hostnameOutput.replace("\n", "")
hostnameOutput = hostnameOutput.split(".", 1)

output+= "Hostname:\t\t" + hostnameOutput[0] + "\n"
output+= "Domain:\t\t\t" + hostnameOutput[1] + "\n"
output+="\n"

ipAddr = subprocess.run(args=["ip", "route"], stdout=subprocess.PIPE).stdout.decode('utf-8')
ipAddr = ipAddr.split(" ", 4)

gate = subprocess.run(args=["netstat", "-rn"], stdout=subprocess.PIPE).stdout.decode('utf-8')
gate = gate.split("\n")
gate = gate[2][16:32].strip()

output+= "Network Information\n"
output+= "IP Address:\t\t" + ipAddr[2] + "\n"
output+= "Gateway:\t\t" + gate + "\n"
output+= "Network Mask:\t\t"
output+= "DNS1:\t\t"
output+= "DNS2:\t\t"
output+= "\n"

output+= "Operating System Information\n"
output+= "Operating System:\t\t"
output+= "OS Version:\t\t"
output+= "Kernel Version:\t\t"
output+= "\n"

output+= "Storage Information\n"
output+= "System Drive Total:\t"
output+= "System Drive Used:\t"
output+= "System Drive Free:\t"
output+= "\n"

output+= "Processor Information\n"
output+= "CPU Model:\t\t\t"
output+= "Number of processors:\t"
output+= "Number of cores:\t\t"
output+= "\n"

output+= "Memory Information\n"
output+= "Total RAM:\t\t\t"
output+= "Available RAM:\t\t"

print(output)
