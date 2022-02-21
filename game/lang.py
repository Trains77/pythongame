import sys
import pathlib
from shared import language, fallback_lang_only

current_path = pathlib.Path().parent.absolute()
sys.path.insert(1, str(current_path) + '/Language')
from fallback import *
if fallback_lang_only == False:
    if language == "english":
        from english import *
    else:
        print("invalid_lang_error")
