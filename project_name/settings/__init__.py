try:
	from .local import *
except Exception as e:
	print("no locale.py settings file. import dev settings.")
	from .dev import *

