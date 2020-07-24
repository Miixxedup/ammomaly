from utils.local_portscan import *
from utils.state import *
import psutil
from pprint import pprint
from time import sleep
import argparse

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

    # Stupid tracking loop
    i = 0
    while i < 10:
        update_states()
        sleep(5)
        i+=1

#Argparse 
parser = argparse.ArgumentParser()
parser.add_argument(
    '-m','--modules',
    action = 'store_true',
    default = False, 
    dest= 'module_switch',
    help = "Start ammomaly with all .py modules from the module folder")
parser_results = parser.parse_args()

# import all modules and go, otherwise execute above loop
if parser_results.module_switch:
    print("Starting all modules found in:")
else:
    print("Starting the manual defined loop in ammomaly.py")
    manual_call()