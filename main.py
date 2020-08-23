from ammomaly import parser_results
from utils.local_portscan import *
from utils.state import *
from utils.load_modules import *
from config import *
from time import sleep
from assets.logo import *
import psutil

# Update loop
# Stupid tracking loop for now
# Stops after 10 iterations
def update():    
    i = 0
    while True:
        update_states()
        sleep(DEFAULT_REFRESH_TIME)
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

print(logo_string)
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