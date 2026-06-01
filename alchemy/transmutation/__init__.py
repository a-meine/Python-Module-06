"""
Absolute import does not work on packages by default
this is why we need to load the modules using
__init__.py aka package initialiser
"""
# print("let's init transmutation")

from . import recipes

__all__ = ["recipes"]
