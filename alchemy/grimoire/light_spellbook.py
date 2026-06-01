from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # print("light_spellbook: start importing validate_ingredients()")
    # from . import validate_ingredients
    if validate_ingredients(ingredients) == "VALID":
        return "Spell Recorded Successfully!"
    else:
        return "Spell Couldn't Be Recorded"


"""
Bad option:
"""

# from .light_validator import validate_ingredients


# def light_spell_allowed_ingredients() -> list[str]:
#     return ['earth', 'air', 'fire', 'water']


# def light_spell_record(spell_name: str, ingredients: str) -> str:
#     # print("light_spellbook: start importing validate_ingredients()")
#     # from . import validate_ingredients
#     if validate_ingredients(ingredients) == "VALID":
#         return "Spell Recorded Successfully!"
#     else:
#         return "Spell Couldn't Be Recorded"
