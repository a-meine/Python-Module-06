#!/usr/bin/env python3

"""
Here we are doing: specific import + absolute on a module
this means we have to: say from ...import ... and we specfiy
names/bindings we want the path of the module will  the path
starting from root

    Absolute: means starting from root (aka sys.path[0])
    genral: means we have to to specify everythong in import
        line but we don;t need to mention the name of import
        if it is used directly (eg a function)
    we are running script directly ==> sys.path[0] = folder
    containing the script
"""
from elements import create_water


print(" ===Using absolute import + sepecific import on a module=== \n\n",
      create_water())
