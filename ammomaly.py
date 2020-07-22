from utils.local_portscan import *
from utils.state import *
import psutil
from pprint import pprint
from time import sleep

# Create a new state new_ports
# Generate the data using restruct_tuples()
# Test the differences using merge_diff()
# Add an action start_tcpdump when a difference occures
init_tracking(
    statename= 'new_ports', 
    function_generate= restruct_tuples,
    function_compare= merge_diff, 
    action_on_hit= start_tcpdump
    )

# Stupid tracking loop
i = 0
while i < 10:
    update_states()
    sleep(5)
    i+=1