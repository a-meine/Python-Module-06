#!/usr/bin/env python3

"""
Accessing element in a submodule in a subpackage
This is the exact same as ft_alembic_3.py"""
from alchemy import potions

print("=== Distillation 0 ===")

print("Accessing element in a submodule (complete submodule)\n")
print("Testing strength_potion: ",
      potions.strength_potion())
print("Testing healing_potion: ",
      potions.healing_potion())
