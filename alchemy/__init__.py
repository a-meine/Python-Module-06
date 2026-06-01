# print("[alchemy] starting package instialisation..")


# from .grimoire import light_spellbook
# from .grimoire import light_validator
# print("alchemy: grimore Initialisation complete")

from .elements import create_air
from . import grimoire
from .potions import strength_potion
from .potions import healing_potion as heal
from . import transmutation


# print("[alchemy] package initialisation complete")

__all__ = ["create_air", "strength_potion", "heal", "transmutation",
           "grimoire", "light_spellbook"]

# the following would be nice but tools already recognise
# the above one
# __all__ = [create_air.__name__]  # this is
