from time import sleep

from Ammomaly.config.config import *
from Ammomaly.utils.local_portscan import *
from Ammomaly.ammomaly_core.load_modules import *
from Ammomaly.ammomaly_core.state import *
from Ammomaly.utils.logger import log

''' 
Update loop
Stupid tracking loop for now
Stops after 10 iterations
'''
def update():    
    i = 0
    while True:
        update_states()
        sleep(DEFAULT_REFRESH_TIME)
        i+=1

'''
Create a new state new_ports
Generate the data using restruct_tuples()
Test the differences using merge_diff()
Add an action start_tcpdump when a difference occures
'''
def manual_call():
    init_tracking(
        statename= 'new_ports', 
        function_generate= restruct_tuples,
        function_compare= merge_diff, 
        action_on_diff= start_tcpdump
    )

def main_loop(module_switch):
    # import all modules and go, otherwise execute above loop
    if module_switch:
        log.info("Starting all modules found in ammomaly_modules")
        # Collect all modules with their definitions
        mods = get_all_modules()
        for m in mods:
            log.info(f"Loading {m}") 
            init_tracking(
            statename= m, 
            function_generate= getattr(mods[m][0],mods[m][1]['generate']),
            function_compare= getattr(mods[m][0],mods[m][1]['diff']), 
            action_on_diff= getattr(mods[m][0],mods[m][1]['action'])
        )
    else:
        log.info("Starting the manual defined loop in ammomaly.py")
        manual_call()
    update()
