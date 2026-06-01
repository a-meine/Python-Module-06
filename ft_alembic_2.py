#!/usr/bin/env python3

"""
Here we are doing: general import + absolute on a submodule in a subpackage
this means we have to: say import ... and
the path of the module will  the path starting from root

    Absolute: means starting from root (aka sys.path[0])
    genral: means we didn' specify a name/binding

    we are running script directly ==> sys.path[0] = folder
    containing the script

    The refrence is whatever after from: each time we need
    a binding can say alchemayelement.binding_name
"""
import alchemy.elements

print(" ===Using absolute import + genral import on a module in a",
      "package=== \n\n",
      alchemy.elements.create_earth())
