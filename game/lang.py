import sys
import pathlib
from shared import language

current_path = pathlib.Path().parent.absolute()
sys.path.insert(1, str(current_path) + '/Language')
if language == "en_us":
    from en_us import *
else:
    print("invalid_lang_error")
