from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debugger add
import builtins
from pdb import set_trace

builtins.st = set_trace
