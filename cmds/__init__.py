"""
sets __all__ to all files in the 'cmds' directory.
all commands are imported with ( from cmds import * )
"""

from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]