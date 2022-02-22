# This file is meant to make it easier to modify different texts in the game
from english import *
from shared import language

if language == "english":
    from english import *
else:
    print("invalid_lang_error")
