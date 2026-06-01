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

Option 3: importing the complete module:
    this works because we importing modules:
        - The module is added to sys.modules (even if empty)
        - After passing this bottleneck each dependecy finsh
            initialisation
        - Each one has all their need names
        - At runtime they can starting to access the names
    This oppo


Option 1: importing a complete module"""

from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    """here the fucntion takes  a list of ingredients a single
    str, although it makes it easier for caller to type anything
    it however shifts the focus from import to str operations
    the same way case sensitivity does"""
    allowed: list[str] = light_spellbook.light_spell_allowed_ingredients()
    ings_lowered: list[str] = [ing.lower() for ing in ingredients.split()]
    if any(ing in allowed for ing in ings_lowered):
        return "VALID"
    return "INVALID"


# """
# Option 2: Delaying import: importing in non-import-time code
# note: this might be tedious if you need to use many times"""


# def validate_ingredients(ingredients: str) -> str:
#     """here the fucntion takes  a list of ingredients a single
#     str, although it makes it easier for call to type anything
#     it however shifts the focus form import to str operations
#     the same way case sensitivity does"""
#     from .light_spellbook import light_spell_allowed_ingredients
#     allowed: list[str] = light_spell_allowed_ingredients()
#     ings_lowered: list[str] = [ing.lower() for ing in ingredients.split()]
#     if any(ing in allowed for ing in ings_lowered):
#         return "VALID"
#     return "INVALID"


# print("last line of module: light_validator")


"""Bad option:
"""

# from .light_spellbook import light_spell_allowed_ingredients


# def validate_ingredients(ingredients: str) -> str:
#     """here the fucntion takes  a list of ingredients a single
#     str, although it makes it easier for call to type anything
#     it however shifts the focus form import to str operations
#     the same way case sensitivity does"""
#     allowed: list[str] = light_spell_allowed_ingredients()
#     ings_lowered: list[str] = [ing.lower() for ing in ingredients.split()]
#     if any(ing in allowed for ing in ings_lowered):
#         return "VALID"
#     return "INVALID"
