#!/usr/bin/env python3

# print("starting the import cycle from excuted script ...")
import alchemy.grimoire  # here we are importing a package so ...
# print("finshed importing cycle from excuted script")

# import sys
# print(dir(sys.modules['alchemy.grimoire']))

print(alchemy.grimoire.light_spellbook.light_spell_record("Spell1", "water"))

"""" to see list of names in the module"""
# import sys
# import alchemy.grimoire.light_spellbook
# print("list of names in light_spellbook:")
# print(dir(sys.modules['alchemy.grimoire.light_spellbook']))
