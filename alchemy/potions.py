#!/usr/bin/env python3
from .elements import create_air, create_earth
# using from ..elements will rasie ImportError
# this happens as we try to import outside the package
# without having a parent package
from elements import create_fire, create_water


def healing_potion() -> str:
    return ("Healing potion brewed with " +
            f"’{create_earth()}’ and ’{create_air()}’")


def strength_potion() -> str:
    return ("Strength potion brewed with " +
            f"’{create_fire()}’ and ’{create_water()}’")
