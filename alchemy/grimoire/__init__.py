# print("[grimoire] starting package instialisation..")
# from . import light_validator

# __all__ = ["light_validator"]
"""
Option 1:
Importing importing complete modules
could be done either here or in the module itself"""
from . import light_spellbook
# from . import dark_spellbook

__all__ = ["light_spellbook", "dark_spellbook"]

"""you can also add other names in this API (eg. aliasing purpose):"""
# from .light_validator import validate_ingredients
# from .light_spellbook import light_spell_allowed_ingredients
# __all__ = ["validate_ingredients", "light_spellbook",
#            "light_spell_allowed_ingredients"]

"""Option 2: delayed import in one of them
see: grimoire/light_validator --uncomment option 2"""

"""
Addiotnally: you can import in the parent package
in alchemy/__init__.py uncomment:
# from .grimoire import light_spellbook

"""


"""Other options include modifying the project structure which might not
be allowed as per requirments"""
