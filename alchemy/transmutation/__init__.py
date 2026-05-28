"""
Absolute import does not work on packages by default
this is why we need to load the modules using
__init__.py aka package initialiser
"""
from . import recipes

__all__ = ["recipes"]
