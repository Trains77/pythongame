# Script Modules
import platform
import sys
# import getpass
import colored
from colored import fore, back, style
# import time
# import os
# Script Variables DO NOT TOUCH
system_required = "Linux"
# system_unsupported = "Windows"

# Script Settings
from shared import enable_os_restrictions

# This script was made in linux, it may not work on other operating systems

# print(fore.GREEN,"Hello", getpass.getuser(), style.RESET)
# OS Checker
if enable_os_restrictions == 1:
    if platform.system() == system_required:
        supported = True
# Seperator thing
if enable_os_restrictions == 1:
    if not platform.system() == system_required:
        print( "Sorry, your", platform.system(), "system is not supported by this script!")
        supported = False
        print()
        print(fore.WHITE + back.RED + style.BOLD + "ERROR: UNSUPPORTED_OPERATING_SYSTEM" + style.RESET)
        exit()

if not platform.system() == system_required:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this script" + style.RESET)

#
import music
import game
