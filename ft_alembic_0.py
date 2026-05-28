#!/usr/bin/env python3

"""
Here we are doing: general (aka non-specific) + absolute
on a module (not a package) this means we have to: say import (without from)
and the path of the module will  the path starting from root

    Absolute: means starting from root (aka sys.path[0])
    genral: means we have everything in the module but
        we need name it every time we need something
        eg: elements.create_water()

    we are running script directly ==> sys.path[0] = folder
    containing the script

    here are all the cases of sys.path according to docs

    Root (aka: sys.path[0]) is either

        The directory containing the running script OR
        The current working directory which happens in the following cases:
            Interactive shell (REPL)
            python -c aka code excution as a string from terminal
            python -m aka running a module as a script

    source: https://docs.python.org/3/library/sys_path_init.html

"""
import elements
# import sys

print(" ===Using absolute import + general import on a module=== \n\n",
      elements.create_fire())

# print(sys.path[0])
