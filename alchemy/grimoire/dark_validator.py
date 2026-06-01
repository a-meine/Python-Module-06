"""
This is a classical example of a circular import:
    light_validator needs to import light_spellbook
    and vice versa. here mulutiple way to solve this:
        - Import one inside the function that used it
            this way the import will happen only when funciton is
            called which is by default in series and in prallel
        -

# print("[light_validatpr] starting import from light_spellbook")
# from . import light_spell_allowed_ingredients
# print("[light_validator] light_spellbook import complete")

# """
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """here the fucntion takes  a list of ingredients a single
    str, although it makes it easier for call to type anything
    it however shifts the focus form import to str operations
    the same way case sensitivity does"""
    allowed: list[str] = dark_spell_allowed_ingredients()
    ings_lowered: list[str] = [ing.lower() for ing in ingredients.split()]
    if any(ing in allowed for ing in ings_lowered):
        return "VALID"
    return "INVALID"
