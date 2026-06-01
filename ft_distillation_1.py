#!/usr/bin/env python3

import alchemy

print("=== Distillation 1 ===")
"""The first part is the exact same as ft_alembic_4.py"""
print("Accessing exposed names from a submodule in a subpackage\n")

print("Testing strength_potion:", alchemy.strength_potion())
print("\nAccessing names using alias\n")
print("Testing heal alias:", alchemy.heal())
