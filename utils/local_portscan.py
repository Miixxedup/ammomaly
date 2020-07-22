import psutil
import pandas as pd
from utils.helpers import *

# Restruct the tuples to only get the required information.
def restruct_tuples():
    store_array = [] 
    for p in psutil.net_connections():
        store_array.append([
            safe_lookup(p.laddr)[0],
            safe_lookup(p.laddr)[1],
            safe_lookup(p.raddr)[0],
            safe_lookup(p.raddr)[1],
            p.pid,
            p.fd,
            p.status,
            p.family,
            p.type
        ]) 
    # Store as DataFrame
    df = pd.DataFrame(
        data = store_array,
        columns = ['laddr_ip','laddr_port','raddr_ip','raddr_port','pid','fd','status','family','type']
        )
    # Get the name for the process
    df['pid_name'] = df.pid.apply(lambda x : match_pid_processname(x))
    # Fill NaN
    df.fillna('-', inplace=True)
    # order by laddr
    df.sort_values(by=['laddr_ip'], inplace = True)
    return df

# Look for the name associated with the pid number
def match_pid_processname(pid):
    for proc in psutil.process_iter():
        if proc.pid == pid:
            return proc.name()

def merge_diff(main_df, new_df):
    hits = main_df.merge(new_df, indicator = True, how='outer')
    return hits[hits['_merge'] == 'right_only']

def start_tcpdump(*args):
    print(f"Starting tcpdump using arguments: {[f for f in args]}")
    # TODO implement actual TCPDUMP startup.
    # subproces.Popen(tcpdump, '')