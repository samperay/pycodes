""" 
Prints the system information relates to CPU
Disk, Memory, Network IP address, System Boot time  ..etc
 
"""

import platform
import datetime
import psutil

print("Computer Name:",platform.node())
print("Computer Architecture:",platform.machine())
print("Processor Type:",platform.processor())
print("OS Release:",platform.system())
print("platform:",platform.platform())
print("Kernel Release:",platform.release())
print("Python Version:",platform.python_version())
print("Python compiler:",platform.python_compiler())

# Print CPU count
print("Physical Cores of CPU:",psutil.cpu_count(logical=False))

# To print physical memory
total_phymem=psutil.virtual_memory()[0]
phymem_gb = int(total_phymem/1024/1024/1204)
print("Physical Memory:",phymem_gb,"GB")

# To print swap memory
total_swapmem=psutil.swap_memory()[0]
swapmem_gb = int(total_swapmem/1024/1024/1024)
print("Swap Memory:",swapmem_gb,"GB")

# Print System boot time
systemboottime = psutil.boot_time()
boottimeformat = datetime.datetime.fromtimestamp(systemboottime).strftime("%Y-%m-%d %H:%M:%S")
print("System Boot time:",boottimeformat)

# To Print File system
totalDisks = psutil.disk_partitions(all=False)
print("\nDisk File System information")
print("-----------------------")
for line in totalDisks:
    print(line[0],":",line[1])

# To print Network information
netstats = psutil.net_if_addrs()
intcount = len(netstats.keys())

# To print Network interface names and associated IP
print("\nNetwork Information")
print("--------------------")
print("Network Interfaces:", intcount)

print("\nInterface names and IP:\n")
for intips in netstats.keys():
    print(intips,":",netstats[intips][0][1])


# Print number of users logging to system
print("\nLogon information")
print("------------------")

userscount = len(psutil.users())
print("users logged in system and they are ...",userscount)
# Users logged are
for userlogcount in psutil.users():
    username = userlogcount[0]
    s_time = userlogcount[3]
    s_time_format = datetime.datetime.fromtimestamp(s_time).strftime("%Y-%m-%d %H:%M:%S")
    print("username:",username,"| Login time:",s_time_format)
