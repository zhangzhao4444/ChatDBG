import os
import pathlib
import sys

the_path = pathlib.Path(__file__).parent.resolve()

sys.path.insert(0, os.path.abspath(the_path))

from .chatdbg_ipdb import *

import ipdb

ipdb.__main__._get_debugger_cls = lambda : ChatDBG

def main():
    ipdb.__main__.main()