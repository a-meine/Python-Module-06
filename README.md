# Python Imports

This project is about imports in Python.

## Import key terms

- **Package** = a folder with at least one module; it may contain `__init__.py` (optional im most cases since Python 3.3+) (see below)
- **Module** = a file, `anything.py`
- **Name** = a specfic name of part of the module, like: a function name, a class names, a variable names etc..
- **Root (aka: sys.path[0])** = the main root path of Python (`sys.path`), which is either
  1. The directory **containing the running script** OR
  2. The current working directory which happens in the following cases:
    - Interactive shell (**REPL**)
    - ```python -c``` aka code excution as a string from terminal
    - ```python -m``` aka running a module as a script ( you need: `cd parent_of_my_package` then `pythom -m parent.module`)
- **Absolute import** = when the module/package is referenced starting from root, for example `package.module`, with `package` as `root/package`
- **Relative import** = when the module/package is referenced starting from the importing folder; the importing location is `.`, so to access something from the same folder, `.` is used, and for something from the upper directory, `..` is used

### Absolute vs relative

- If the importing file moves:
  - Relative will break
  - Absolute will work as long as the program is excuted from root and given no manual alteration of sys.path

- If the program executor changes directory:
  - BOTH will break


### specific name vs general import

- **Specific import** = when we use `from` and access a specific module/element from a package, or a specific element from a module; it is done with:
  ```python
  from pack_or_mod import name
  ```
- **General (non-specific) import** = when we import a complete module/package

- **Advantage of module/package import** = we have access to the complete module/package, but we still need to reference it with every name/binding; for example, to use `add`, we have to say `module_name.add`
- **With specific import** = we do not need to mention the name of the module or package, but the downside is that we have to list everything we need in the import line


The only issue with absolute imports is that they are too verbose, while relative imports are concise.

Relative imports are also beneficial for internal package imports, since they always stay fixed relative to each other..

## Package Initialiser aka ``__init__.py`` ##

 ```__init__.py``` is optional since python 3.3 or something, but it needed in the following cases:
  - initlisation code" eg. configuratio
  - API design: exposing subpackages' modules in the top-level
  - Control Wildcard using `__all__`
  - Namespace managment
  - similar cases...


# Import Time vs Runtime

## Import time: all top-level statments:
  - Imports
  - variable assignments outside any func def
  - func/class def
  - clas body (NOT function body)

so if any depandant import happens outside this then circular import will be avoided, eg import inside function body

## Runtime: all the rest basically:
  - function body when called
  - class intantiation
  - etc..


## Sources

  - https://openpython.org/articles/python-modules-and-imports-guide



# To Be Organised:
  - we definetely need them to expose names directly
