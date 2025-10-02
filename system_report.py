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

mask = subprocess.run(args=["ifconfig"], stdout=subprocess.PIPE).stdout.decode('utf-8')
mask = mask[mask.find("netmask")+8:mask.find("broadcast")-1].strip()

dns = subprocess.run(args=["cat", "/etc/resolv.conf"], stdout=subprocess.PIPE).stdout.decode('utf-8')
dns = dns.split("nameserver")
dns1 = dns[1].replace("\n", "").strip()
dns2 = dns[2].replace("\n", "").strip()

output+= "Network Information\n"
output+= "IP Address:\t\t" + ipAddr[2] + "\n"
output+= "Gateway:\t\t" + gate + "\n"
output+= "Network Mask:\t\t" + mask + "\n"
output+= "DNS1:\t\t\t" + dns1 + "\n"
output+= "DNS2:\t\t\t" + dns2 + "\n"
output+= "\n"

osInfo = subprocess.run(args=["cat", "/etc/os-release"], stdout=subprocess.PIPE).stdout.decode('utf-8')
os = osInfo[osInfo.find("PRETTY_NAME=")+13:]
os = os[:os.find("\n")-1]

osVer = osInfo[osInfo.find("VERSION_ID=")+12:]
osVer = osVer[:osVer.find("\n")-1]

kernel = subprocess.run(args=["uname", "-r"], stdout=subprocess.PIPE).stdout.decode('utf-8')

output+= "Operating System Information\n"
output+= "Operating System:\t" + os + "\n"
output+= "OS Version:\t\t" + osVer + "\n"
output+= "Kernel Version:\t\t" + kernel + "\n"
output+= "\n"

systemDrive = subprocess.run(args=["df", "-BGiB", "--total"], stdout=subprocess.PIPE).stdout.decode('utf-8')
systemDrive.split("\n")
systemDrive = systemDrive[len(systemDrive)-1]
systemDrive = systemDrive[6:len(systemDrive)-2].strip()
print(systemDrive)

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
