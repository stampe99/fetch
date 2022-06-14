import cpuinfo
from colorama import Fore
import platform
import psutil
import os
import distro

class Variables():
    try:
        shell = os.environ['SHELL'].replace("/usr/bin/", "").lower()
    except:
        shell = "unknown"
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        CPU = proc["brand_raw"].lower()
    except:
        CPU = "unknown"
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        Bit = proc["arch_string_raw"].lower()
    except:
        Bit = "unknown"
        pass
    try:
        ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" gb"
    except:
        ram = "unknown"
        pass
    try:
        User = os.environ['USER'].lower()
    except:
        pass
        User = "unknown"
    try:
        distr = distro.linux_distribution()[0].lower()
    except:
        distr = "unknown"
        pass
    try:
        if os.environ['XDG_CURRENT_DESKTOP'] and os.environ['DESKTOP_SESSION']:
            GUI = os.environ['XDG_CURRENT_DESKTOP'].lower() +  ", " + os.environ['DESKTOP_SESSION'].lower()
    except:
        GUI = "unknown"
        pass
    try:
        term = os.environ["TERM"].lower()
    except:
        term = "powershell" # If it's not set, it's probably a Windows terminal if you're on windows
        pass
    try:
        pc_name = os.environ['COMPUTERNAME'].lower()
    except:
        pc_name = "unknown"
        pass


"""
def getUptime():
    return os.system("uptime")
print(getUptime())
uptime = getUptime()
"""
