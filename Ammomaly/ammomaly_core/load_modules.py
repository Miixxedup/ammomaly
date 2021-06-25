from importlib import import_module
from os import listdir
from os.path import isfile
from pprint import pprint

# Method to loop over ammomaly_modules and import all.
IGNORE_FILES = ['__init__.py','example_module.py',"__pycache__"]
MUST_CONTAIN = ['_generate','_diff','_action']
DIRECTORY = 'ammomaly_modules'

def get_all_modules():
    modules = dict()
    # Tuples containing the package and the name
    to_import = [(import_module(f"{DIRECTORY}.{l[:-3]}"),l[:-3]) for l in listdir("ammomaly_modules") if l not in IGNORE_FILES]
    # Import the package and name into a dict
    for d in to_import:
        modules[d[1]] = d[0]
    # Check if all modules contain all required methods and create a new dict containing all the information
    for m in modules:
        modules[m] = (modules[m], required_defs(modules[m]))
    return modules

# Get all the defs from a module
# Assuming naming conventions are followed
def required_defs(m):
    defs = dir(m)
    def_names = dict()
    for d in defs:
        for m in MUST_CONTAIN:
            if m in d:
                def_names[m[1:]] = d
    return def_names
