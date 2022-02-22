# This file is meant to make it easier to modify different texts in the game
from fallback import *
from shared import fallback_lang_only, language

if fallback_lang_only == False:
    if language == "english":
        from english import *
    else:
        print("invalid_lang_error")
