# Script Modules
import platform
import sys
import colored
from colored import fore, back, style
system_required = "Linux"

# Script Settings
from shared import enable_os_restrictions, enable_program

# This script was made in Linux, it may not work on other operating systems

# OS Checker
if enable_os_restrictions == 1:
    if platform.system() == system_required:
        supported = True
if enable_os_restrictions == 1:
    if not platform.system() == system_required:
        print( "Sorry, your", platform.system(), "system is not supported by this script!")
        supported = False
        print()
        print(fore.WHITE + back.RED + style.BOLD + "ERROR: UNSUPPORTED_OPERATING_SYSTEM" + style.RESET)
        exit()
if not platform.system() == system_required:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this script" + style.RESET)

if enable_program == True:
    import music
    import game
elif enable_program == False:
    print("Game has been disabled in shared.py")

# Hello Nerds!
