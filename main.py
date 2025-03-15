#!/usr/bin/python3
import os
import math
import urllib.request
import sys
import json

version = "1.0.1"

url = "https://raw.githubusercontent.com/SnowsSky/snowfetch/main/versions.json"


with urllib.request.urlopen(url) as response:
    data = response.read().decode("utf-8")

rep = json.loads(data)

latest_ver = rep[0]["version"]

#Colors 
RED = '\033[1;38;5;124m'
LIGHT_ORANGE = "\033[1;38;2;255;165;0m"
LIGHT_VIOLET = "\033[1;38;2;169;154;205m"
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = "\033[1;38;2;44;114;199m"
CYAN = '\033[1;96m'
LIGHT_GREEN = "\033[1;38;2;144;238;144m"
BLURPLE = '\033[1;38;5;63m'
RESET = '\033[0m'
os_color = None
import argparse
if version <= latest_ver: 
    print(f"{LIGHT_ORANGE}Please Update Snowfetch{version} --> Snowfetch{latest_ver}{RESET}")



with open("/etc/os-release") as f:
    os_release = {line.split("=")[0]: line.split("=")[1].strip().strip('"') for line in f if "=" in line}
os_name = os_release.get("PRETTY_NAME", "None") 
os_home_url = os_release.get("HOME_URL", "None") 
os_s_name = os_release.get("NAME", "None")



#OS COLOR
if os_s_name == "AdOS": os_color = BLURPLE
else : print(f"{LIGHT_ORANGE}Oh, it looks like you're not using AdonixOS ):{RESET}")
if "Arch Linux" in os_s_name : os_color = CYAN
elif "Ubuntu" in os_s_name : os_color = LIGHT_ORANGE
elif "Debian" in os_s_name : os_color = RED
elif "Fedora" in os_s_name or "elementary OS" in os_s_name : os_color = '\033[1;38;5;32m'
elif "Manjaro Linux" in os_s_name or "Linux Mint" in os_s_name or "openSUSE" in os_s_name: os_color = LIGHT_GREEN
elif "CentOS Linux" in os_s_name : os_color = LIGHT_RED
elif "Gentoo" in os_s_name: os_color = LIGHT_VIOLET
elif "AlmaLinux" in os_s_name : os_color = BLUE



def parse_args():
    parser = argparse.ArgumentParser(description="Choose a color and a distribution.")
    parser.add_argument("--color", type=str, choices=["RED", "ORANGE", "GREEN", "VIOLET", "BLURPLE", "BLUE", "CYAN"], required=False, help="Choose a color from: RED, ORANGE, GREEN, VIOLET, BLURPLE, BLUE, CYAN")
    return parser.parse_args()
args = parse_args()

#Manual Colors
if args.color : 
    if str(args.color).upper() == "RED":
        os_color = RED
    elif str(args.color).upper() == "ORANGE":
        os_color = LIGHT_ORANGE
    elif str(args.color).upper() == "GREEN":
        os_color = LIGHT_GREEN
    elif str(args.color).upper() == "VIOLET":
        os_color = LIGHT_VIOLET
    elif str(args.color).upper() == "BLURPLE":
        os_color = BURPLE
    elif str(args.color).upper() == "BLUE":
        os_color = BLUE
    elif str(args.color).upper() == "CYAN":
        os_color = CYAN
        

        

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
mem_usage_percent = round((mem_used / mem_total * 100)) if mem_total > 0 else 0
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
disk_used_percent = round((disk_used / disk_total * 100)) if disk_total > 0 else 0

# Uptime
with open("/proc/uptime") as f:
    uptime_seconds = float(f.readline().split()[0])
uptime_hours = int(uptime_seconds // 3600)
uptime_minutes = int((uptime_seconds % 3600) // 60)

#Get user
user = os.getlogin()


print(f"{BLURPLE}@SnowFetch {version}{RESET}") 


print(f"{os_color}💻 OS ->{RESET} {os.uname().sysname}, {os_name} : \033[4;96m{os_home_url}{RESET}")
print(f"{os_color}🔄 Version ->{RESET} {os.uname().version}")
print(f"{os_color}🐧 Kernel ->{RESET} {os.uname().release}")
print(f"{os_color}📦 Package manager ->{RESET} {Package_Manager}")
print(f"{os_color}🌐 Hostname ->{RESET} {os.uname().nodename}")
print(f"{os_color}🚹 Username ->{RESET} {user}")
print(f"{os_color}⚙️  CPU -> {RESET} {cpu_name} | {cpu_cores} Cores")
if uptime_hours >= 1:
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_hours}h(s)")
elif uptime_minutes >= 3 :
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_minutes}mins")
else :
    print(f"{os_color}🕒 Uptime ->{RESET} {uptime_seconds}seconds")
print(f"{os_color}🧠 Memory ->{RESET} {round(mem_used)} / {round(mem_total)} MB ({mem_usage_percent}%)")
print(f"{os_color}💾 Disk ->{RESET} {disk_used} / {disk_total} GB ({disk_used_percent}%)")
