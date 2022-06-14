from colorama import Fore
import platform
import sys
import ctypes
import os
from osinfo import Variables

lib = ctypes.windll.kernel32
t = lib.GetTickCount64()
t = int(str(t)[:-3])

# Emojis ( Unicode )

balloon = '\U0001F388'
rocket = '\U0001F680'
ufo = '\U0001F6F8'
fire = '\U0001F525'
planet = '\U0001FA90'
time = '\U0001F319'
color1 = '\U0001F3B2'
color2 = '\U0001F9E9'
mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

# Colors

reset = Fore.RESET
lyellow = Fore.LIGHTYELLOW_EX
yellow = Fore.YELLOW
green = Fore.GREEN
cyan = Fore.CYAN
red = Fore.RED
magenta = Fore.MAGENTA
black = Fore.BLACK
blue = Fore.BLUE
white = Fore.WHITE

new = rf'''
{lyellow}     .--.         {lyellow + Variables.pc_name + reset + "@" + lyellow + platform.system() + reset}
{lyellow}    |{reset}o_o{lyellow} |        {green + "terminal" + red + " -> " + reset + Variables.term}
{lyellow}    |{Fore.RED}:_/{lyellow} |        {green + "cpu" + red + " -> " + reset + Variables.CPU}
{lyellow}   //   \ \       {green + "memory" + red + " -> " + reset + Variables.ram}
{lyellow}  (|     | )      {green + "uptime" + red + " -> " + reset + f"{days} days, {hour:02}:{mins:02}:{sec:02}"}
{lyellow} /'\_   _/`\
{lyellow} \___)=(___/      {black +"███" + reset}{red +"███" + reset}{green +"███" + reset}{yellow +"███" + reset}{blue +"███" + reset}{magenta +"███" + reset}{cyan +"███" + reset}{white +"███" + reset}

'''
print(new)
