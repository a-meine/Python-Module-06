#!/usr/bin/env python3

# print("starting the import cycle from excuted script ...")
try:
    # import alchemy.grimoire
    from alchemy.grimoire import dark_spellbook
except ImportError:
    print("[ImportError]:you trying to import names from an incomplete",
          "module, to solve this:",
          "\n1. Import a complete module instead of a specific name",
          "\n2. Delay one of the imports by putting it in non-imprt-time code",
          "\n3. If modules are so interconnected, merge them in one module")
    exit()
print(dark_spellbook.dark_spell_record("Spell1", "NOT-arsenic"))
# print("finshed importing cycle from excuted script")

"""" to see list of modules names in the module"""
# import sys
# print(dir(sys.modules['alchemy.grimoire']))
# print("trying to access modules  in a circular import...")

# import alchemy.grimoire.light_spellbook
# print("list of names in light_spellbook:")
# print(dir(sys.modules['alchemy.grimoire.light_spellbook']))
