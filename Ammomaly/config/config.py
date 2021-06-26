DEFAULT_REFRESH_TIME = 10

# Method to loop over ammomaly_modules and import all.
IGNORE_FILES = ['__init__.py','example_module.py',"__pycache__"]
MUST_CONTAIN = ['generate','diff','action']
MAY_CONTAIN = ['_config']
DIRECTORY = 'Ammomaly/ammomaly_modules/'
IMPORT_DIRECTORY = 'Ammomaly.ammomaly_modules'