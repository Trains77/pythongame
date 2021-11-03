# This script was made in Linux, it may not work on other operating systems

# Script Modules
import platform
import colored
from colored import fore, back, style

# Script Settings
from shared import enable_os_restrictions, enable_program, system_recommends

# OS Checker has been deprecated in v0.07
# if enable_os_restrictions == 1:
#    if platform.system() == system_required:
#        supported = True
# if enable_os_restrictions == 1:
#    if not platform.system() == system_required:
#        print( "Sorry, your", platform.system(), "system is not supported by this script!")
#        supported = False
#        print()
#        print(fore.WHITE + back.RED + style.BOLD + "ERROR: UNSUPPORTED_OPERATING_SYSTEM" + style.RESET)
#        exit()

if not platform.system() == system_recommends:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this program" + style.RESET)

if enable_program == True:
    import music
    import game
elif enable_program == False:
    print("The program has been disabled in shared.py")
    print()
    print(fore.WHITE + back.RED + style.BOLD + "ERROR: GAME_DISABLED" + style.RESET)
