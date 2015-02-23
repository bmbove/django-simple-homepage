from .base import *

try:
    from .local import *
except ImportError:
    print "Error importing local settings"
    pass
