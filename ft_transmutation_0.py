#!/usr/bin/env python3

import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print("access of multi-level packages: submodule in a subpackage;",
      "importing a submodule")
print("Testing lead to gold:", alchemy.transmutation.recipes.lead_to_gold())
