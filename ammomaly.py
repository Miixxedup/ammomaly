from utils.local_portscan import *
from utils.state import *
from utils.load_modules import *
from time import sleep
import psutil
import argparse

# Update loop
# Stupid tracking loop for now
# Stops after 10 iterations
def update():    
    i = 0
    while i < 10:
        update_states()
        sleep(5)
        i+=1


# Create a new state new_ports
# Generate the data using restruct_tuples()
# Test the differences using merge_diff()
# Add an action start_tcpdump when a difference occures
def manual_call():
    init_tracking(
        statename= 'new_ports', 
        function_generate= restruct_tuples,
        function_compare= merge_diff, 
        action_on_diff= start_tcpdump
        )

#Argparse 
parser = argparse.ArgumentParser()
parser.add_argument(
    '-m','--modules',
    action = 'store_true',
    default = False, 
    dest= 'module_switch',
    help = "Start ammomaly with all .py modules from the module folder")
parser.add_argument(
    '-d','--debug',
    action = 'store_true',
    default = False, 
    dest= 'debug_switch',
    help = "Modify program executing to start the debug-path")

parser_results = parser.parse_args()

# Testing grounds -d switch
if parser_results.debug_switch:
    print("[DEBUG] Starting in debug mode:")
    pass
else:
    # import all modules and go, otherwise execute above loop
    if parser_results.module_switch:
        print("[INFO] Starting all modules found in ammomaly_modules:")
        # Collect all modules with their definitions
        mods = get_all_modules()
        for m in mods: 
            init_tracking(
            statename= m, 
            function_generate= getattr(mods[m][0],mods[m][1]['generate']),
            function_compare= getattr(mods[m][0],mods[m][1]['diff']), 
            action_on_diff= getattr(mods[m][0],mods[m][1]['action'])
            )
    else:
        print("Starting the manual defined loop in ammomaly.py")
        manual_call()
    update()