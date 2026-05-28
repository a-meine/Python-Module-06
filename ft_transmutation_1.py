#!/usr/bin/env python3
"""
Absolute import does not work on packages by default
this is why we need to load the modules using
__init__.py aka package initialiser
"""
import alchemy.transmutation


print(alchemy.transmutation.recipes.lead_to_gold())
