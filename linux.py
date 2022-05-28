from colorama import Fore
import platform
import sys
import ctypes
import os
from osinfo import Variables

# Emojis ( Unicode )

balloon = '\U0001F388'
rocket = '\U0001F680'
ufo = '\U0001F6F8'
fire = '\U0001F525'
planet = '\U0001FA90'
time = '\U0001F319'
color1 = '\U0001F3B2'
color2 = '\U0001F9E9'

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

peng = rf'''
{lyellow}     .--.         {lyellow + Variables.User + reset + "@" + lyellow + platform.system() + reset}
{lyellow}    |{reset}o_o{lyellow} |        {green + "Shell" + red + " -> " + reset + Variables.shell}
{lyellow}    |{Fore.RED}:_/{lyellow} |        {green + "Distro" + red + " -> " + reset + Variables.distr}
{lyellow}   //   \ \       {green + "CPU" + red + " -> " + reset + Variables.CPU}
{lyellow}  (|     | )      {green + "Memory" + red + " -> " + reset + Variables.ram}
{lyellow} /'\_   _/`\
{lyellow} \___)=(___/      {black +"███" + reset}{red +"███" + reset}{green +"███" + reset}{yellow +"███" + reset}{blue +"███" + reset}{magenta +"███" + reset}{cyan +"███" + reset}{white +"███" + reset}

'''
print(peng)