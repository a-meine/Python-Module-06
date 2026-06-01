#!/usr/bin/env python3

"""
Here we are doing: general import + absolute on a package
this means we have to: say from ... import ... and
the path of the module will  the path starting from root

    Absolute: means starting from root (aka sys.path[0])
    general: becasue we have to to specify everythong in import
        line but we don;t need to mention the name of import
        if it is used directly (eg a function) i nthis case we
        need elements.create_air() to access it
    The refrence is whatever after from: each time we need
    a binding can say element.binding_name
    we are running script directly ==> sys.path[0] = folder
    containing the script
"""
from alchemy import elements


print(" ===Using absolute import + genral import to import a complete",
      "submodule=== \n\n",
      elements.create_air())


"""OR"""

# from alchemy.elements import create_air

# print(" ===Using absolute import + genral import on a module in a",
#   "package=== \n\n",
#   create_air())
