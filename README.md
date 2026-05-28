# Python Imports

This project is about imports in Python.

## Import key terms

- **Module** = a file, `anything.py`
- **Package** = a folder with at least one module; it may contain `__init__.py` (not required since Python 3.3+), but it is highly recommended and is best practice
- **Root (aka: sys.path[0])** = the main root path of Python (`sys.path`), which is either
  1. The directory **containing the running script** OR
  2. The current working directory which happens in the following cases:
    - Interactive shell (**REPL**)
    - ```python -c``` aka code excution as a string from terminal
    - ```python -m``` aka running a module as a script
- **Absolute import** = when the module/package is referenced starting from root, for example `package.module`, with `package` as `root/package`
- **Relative import** = when the module/package is referenced starting from the importing folder; the importing location is `.`, so to access something from the same folder, `.` is used, and for something from the upper directory, `..` is used
- **sepcifc import

- **Advantage of module/package import** = we have access to the complete module/package, but we still need to reference every name/binding through the imported name; for example, to use `add`, we have to say `module_name.add`
- **With specific import** = we do not need to mention the name of the module or package, but the downside is that we have to list everything we need in the import line

## Specific vs general import

- **Specific import** = when we use `from` and access a specific module/element from a package, or a specific element from a module; it is done with:
  ```python
  from pack_or_mod import ...
  ```
- **General (non-specific) import** = when we import a complete module/package


## Absolute vs relative

- If the importing file moves:
  - Relative will break
  - Absolute will work as long as the program is excuted from root and given no manual alteration of sys.path

- If the program executor changes directory:
  - BOTH will break


The only issue with absolute imports is that they are too verbose, while relative imports are concise.

Relative imports are also beneficial for internal package imports, since they always stay fixed relative to each other..

