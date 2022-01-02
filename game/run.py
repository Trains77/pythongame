# This script was made in Linux, it may not work on other operating systems

# Script Modules
import platform
import colored
from colored import fore, back, style

# Script Settings
from shared import enable_program, system_recommends

if not platform.system() == system_recommends:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this program" + style.RESET)

if enable_program == True:
#    import music
    import game
elif enable_program == False:
    print("The program has been disabled by shared.py")
    print()
    print(fore.WHITE + back.RED + style.BOLD + "ERROR: GAME_DISABLED" + style.RESET)
