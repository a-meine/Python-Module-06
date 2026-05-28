#!/usr/bin/env python3
"""
Here we are doing: absolute import + general on a package
This is possible becasue of the package initialiser which
exposes specific names/bindings.

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
import alchemy

print("Using package intialiser we can access exposed names/bindings")
print("===Using absolute import with general import using",
      " Package initialiser __init__.py===\n\n",
      alchemy.create_air())

print("===Trying to access non-exposed names===\n")

try:
    alchemy.create_earth()
except AttributeError:
    print("Attribute error: create_earth() was not exposed",
          " in the __init__.py")
