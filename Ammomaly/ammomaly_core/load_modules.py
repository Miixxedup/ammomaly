from importlib import import_module
from os import listdir
from Ammomaly.utils.logger import log

# Method to loop over ammomaly_modules and import all.
IGNORE_FILES = ['__init__.py','example_module.py',"__pycache__"]
MUST_CONTAIN = ['generate','diff','action']
MAY_CONTAIN = ['_config']
DIRECTORY = 'Ammomaly/ammomaly_modules/'
IMPORT_DIRECTORY = 'Ammomaly.ammomaly_modules'

def get_all_modules():
    modules = dict()
    # Tuples containing the package and the name
    to_import = [(import_module(f"{IMPORT_DIRECTORY}.{l[:-3]}"),l[:-3]) for l in listdir(DIRECTORY) if l not in IGNORE_FILES]
    # Import the package and name into a dict
    for d in to_import:
        modules[d[1]] = d[0]
    # Check if all modules contain all required methods and create a new dict containing all the information
    for m in modules:
        modules[m] = (modules[m], required_defs(m, modules[m]))
    return modules

# Get all the defs from a module and test if all required are there.
# Assuming naming conventions are followed etc.
def required_defs(m, modules):
    defs = dir(modules)
    def_names = dict()
    for d in defs:
        tmp_d = f"{d.split('_')[-1]}"
        if tmp_d in MUST_CONTAIN or tmp_d in MAY_CONTAIN:
            def_names[tmp_d] = d
    test_requirements(m, def_names)
    return def_names

def test_requirements(module_name, list_of_defs):
    for m in MUST_CONTAIN:
        if m not in list_of_defs:
            assert(f" {module_name} does not have all required classes!")
    log.info(f"Module {module_name} succesfully loaded!")
    