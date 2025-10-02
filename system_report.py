#! usr/bin/python3

# Joshua Krogstad, 10/2/25
import subprocess

# Clear Terminal
subprocess.run("clear")

output = "\t\t\tSystem Report - " + subprocess.run(args=["date", "+%A %W, %Y"], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Find hostname through hostname command
hostnameOutput = subprocess.run("hostname", stdout=subprocess.PIPE).stdout.decode('utf-8')
hostnameOutput = hostnameOutput.replace("\n", "") # Remove newline character
hostnameOutput = hostnameOutput.split(".", 1) # Split into hostname section and domain section

# Add variables to be printed
output+= "\nDevice Information\n"
output+= "Hostname:\t\t" + hostnameOutput[0] + "\n"
output+= "Domain:\t\t\t" + hostnameOutput[1] + "\n"
output+="\n"

# Run new commands to find ip address
ipAddr = subprocess.run(args=["ip", "route"], stdout=subprocess.PIPE).stdout.decode('utf-8')
ipAddr = ipAddr.split(" ", 4) # Split by spaces

# Get routing table with numbers
gate = subprocess.run(args=["netstat", "-rn"], stdout=subprocess.PIPE).stdout.decode('utf-8')
gate = gate.split("\n") # Remove newline character
gate = gate[2][16:32].strip() # Find location of newline, split into before and after possible location of gateway, strip

# run ifconfig
mask = subprocess.run(args=["ifconfig"], stdout=subprocess.PIPE).stdout.decode('utf-8')
mask = mask[mask.find("netmask")+8:mask.find("broadcast")-1].strip() # split into after netmask and before broadcast, strip

# print resolve.conf
dns = subprocess.run(args=["cat", "/etc/resolv.conf"], stdout=subprocess.PIPE).stdout.decode('utf-8')
dns = dns.split("nameserver") # split where it says nameserver
dns1 = dns[1].replace("\n", "").strip() # Use first nameserver, remove newline, strip
dns2 = dns[2].replace("\n", "").strip() # Same for 2nd

# Add variables to be printed
output+= "Network Information\n"
output+= "IP Address:\t\t" + ipAddr[2] + "\n"
output+= "Gateway:\t\t" + gate + "\n"
output+= "Network Mask:\t\t" + mask + "\n"
output+= "DNS1:\t\t\t" + dns1 + "\n"
output+= "DNS2:\t\t\t" + dns2 + "\n"
output+= "\n"

# Print release info
osInfo = subprocess.run(args=["cat", "/etc/os-release"], stdout=subprocess.PIPE).stdout.decode('utf-8')
os = osInfo[osInfo.find("PRETTY_NAME=")+13:] # Find "Pretty Name" and cut everything before it
os = os[:os.find("\n")-1] # Cut everything after the end of Pretty name

osVer = osInfo[osInfo.find("VERSION_ID=")+12:] # Same for version ID
osVer = osVer[:osVer.find("\n")-1] # Cut end of VerID

# Get kernel version
kernel = subprocess.run(args=["uname", "-r"], stdout=subprocess.PIPE).stdout.decode('utf-8').replace("\n", "")

# Add variables to be printed
output+= "Operating System Information\n"
output+= "Operating System:\t" + os + "\n"
output+= "OS Version:\t\t" + osVer + "\n"
output+= "Kernel Version:\t\t" + kernel + "\n"
output+= "\n"

# Get System Drive info
systemDrive = subprocess.run(args=["df", "-BGiB", "--total"], stdout=subprocess.PIPE).stdout.decode('utf-8')
systemDrive = systemDrive[systemDrive.find("total")+6:] # Find only the final 'total' line
firstIndex = systemDrive.find("GiB") # Find index of first occurence of GiB
driveTotal = systemDrive[firstIndex-5:firstIndex+3].strip() # Collect just the first entry
secondIndex = systemDrive.find("GiB", firstIndex+1) # Use first to find 2nd occurence
driveUsed = systemDrive[secondIndex-3:secondIndex+4].strip() # Collect Second entry
thirdIndex = systemDrive.find("GiB", secondIndex+1) # Use 2nd to find 3rd occurence
driveFree = systemDrive[thirdIndex-3:thirdIndex+4].strip() # Third entry

# Add variables to be printed
output+= "Storage Information\n"
output+= "System Drive Total:\t" + driveTotal + "\n"
output+= "System Drive Used:\t" + driveUsed + "\n"
output+= "System Drive Free:\t" + driveFree + "\n"
output+= "\n"

# Get cpu info
cpuInfo = subprocess.run(args=["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE).stdout.decode('utf-8')
cpuModel = cpuInfo[cpuInfo.find("model name"):] # get model name line only
cpuModel = cpuModel[cpuModel.find(":")+1:cpuModel.find("\n")].strip() # move to data part only
cpuProc = subprocess.run(args=["nproc", "--all"], stdout=subprocess.PIPE).stdout.decode('utf-8').replace("\n", "").strip() # get processors number
cpuCores = cpuInfo[cpuInfo.find("cpu cores"):] # get cores number line only
cpuCores = cpuCores[cpuCores.find(":")+1:cpuInfo.find("\n")].strip() # Collect only the final number

# Add variables to be printed
output+= "Processor Information\n"
output+= "CPU Model:\t\t" + cpuModel + "\n"
output+= "Number of processors:\t" + cpuProc + "\n"
output+= "Number of cores:\t" + cpuCores + "\n"
output+= "\n"

# grab output from free command
ramInfo = subprocess.run(args=["free", "-h"], stdout=subprocess.PIPE).stdout.decode('utf-8')
ramInfo = ramInfo[ramInfo.find("Mem:")+5:] # grab only the ram line
ramTotal = ramInfo[:16].strip() # collect the first column
ramAvail = ramInfo[28:41].strip() # collect the third column

# Add variables to be printed
output+= "Memory Information\n"
output+= "Total RAM:\t\t" + ramTotal + "\n"
output+= "Available RAM:\t\t" + ramAvail + "\n"

#Print all collected info
print(output)
#Save to file
output+="\n"
with open(hostnameOutput[0] + "_system_report.log", "w") as file:
    file.write(output)
