#!/usr/bin/env python3
"""
Absolute import does not work on packages by default
this is why we need to load the modules using
__init__.py aka package initialiser
"""
import alchemy.transmutation

print("===Distillation 1===")
print("access of multi-level packages: submodule in a subpackage;",
      "importing a subpackage")
print(alchemy.transmutation.recipes.lead_to_gold())
