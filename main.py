import os
import math
#Colors 
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
LIGHT_CYAN = '\033[1;96m'
BLURPLE = '\033[1;38;5;63m'
RESET = '\033[0m'
os_color = None


with open("/etc/os-release") as f:
    os_release = {line.split("=")[0]: line.split("=")[1].strip().strip('"') for line in f if "=" in line}
os_name = os_release.get("PRETTY_NAME", "None") 
os_home_url = os_release.get("HOME_URL", "None") 
os_s_name = os_release.get("NAME", "None")
#OS COLOR

if os_s_name == "AdOS": os_color = BLURPLE
else : print(f"{RED}Oh, it looks like you're not using AdonixOS ):{RESET}")
if os_s_name == "Arch Linux": os_color = LIGHT_CYAN
elif os_s_name == "Ubuntu": os_color = '\033[1;38;5;214m'
elif os_s_name == "Debian": os_color = '\033[1;38;5;196m'
elif os_s_name == "Fedora" or os_s_name == "elementary OS" : os_color = '\033[1;38;5;32m'
elif os_s_name == "Manjaro Linux" or os_s_name == "Linux Mint" or os_s_name == "openSUSE": os_color = '\033[1;38;5;46m'
elif os_s_name == "CentOS Linux": os_color = '\033[1;38;5;124m'
elif os_s_name == "Gentoo" : os_color = ''
elif os_s_name == "AlmaLinux" : os_color = ''
elif os_s_name == "blendOS": os_color = ''
elif os_s_name == "Rocky Linux": os_color =  ''
#Memory
with open("/proc/meminfo") as f:
    for l in f:
        key, value = l.split(":")[0], l.split(":")[1].strip()
        if key == "MemTotal":
            mem_total = int(value.split()[0]) / 1024  
        elif key == "MemFree":
            mem_free = int(value.split()[0]) / 1024 


mem_total = mem_total if mem_total is not None else 0
mem_free = mem_free if mem_free is not None else 0
mem_used = mem_total - mem_free
cpu_name = None
Package_Manager = None

#Package manager
list = os.listdir("/etc/")
for thing in list:
	if "pacman.conf" in thing or "apt.conf" in thing:
		Package_Manager = thing.split(".conf")[0]


#CPU 
with open("/proc/cpuinfo") as f:
	for l in f:
		if ":" in l:
			key, value = l.split(":", 1) 
			key = key.strip()
			value = value.strip() 
		if key == "model name":
			cpu_name = " ".join(value.split())
		if key == "processor" : 
			cpu_cores = "".join(value.split())

#Disk
stat = os.statvfs("/")
disk_total = stat.f_blocks * stat.f_frsize // (1024 ** 3)
disk_free = stat.f_bavail * stat.f_frsize // (1024 ** 3)
disk_used = disk_total - disk_free

# Uptime
with open("/proc/uptime") as f:
    uptime_seconds = float(f.readline().split()[0])
uptime_hours = int(uptime_seconds // 3600)
uptime_minutes = int((uptime_seconds % 3600) // 60)



print(f"{BLURPLE}@SnowFetch 1.0.0{RESET}") 
print(f"{os_color}💻 OS ->{RESET} {os.uname().sysname}, {os_name} : {os_home_url}")
print(f"{os_color}🔄 Version ->{RESET} {os.uname().version}")
print(f"{os_color}🐧 Kernel ->{RESET} {os.uname().release}")
print(f"{os_color}📦 Package manager ->{RESET} {Package_Manager}")
print(f"{os_color}🌐 Hostname ->{RESET} {os.uname().nodename}")
print(f"{os_color}⚙️  CPU -> {RESET} {cpu_name} | {cpu_cores}Cores")
if uptime_hours >= 1:
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_hours}h")
elif uptime_minutes >= 3 :
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_minutes}min")
else :
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_seconds}s")
print(f"{os_color}🧠 Memory ->{RESET} {round(mem_used)} / {round(mem_total)} MB")
print(f"{os_color}💾 Disk ->{RESET} {disk_used} / {disk_total} GB")
