from shared import language, fallback_lang_only
from fallback import *
if fallback_lang_only == False:
    if language == "english":
        from english import *
    else:
        print("invalid_lang_error")
