import argparse
from Ammomaly.ammomaly_core.loop import *
from Ammomaly.assets.logo import logo_string

def main():    
    
    parser = argparse.ArgumentParser('Ammomaly framework to handle sudden changes in an environment')
    parser.add_argument('-m','--modules', action= 'store_true', default= False, dest= 'module_switch', help= "Start ammomaly with all .py modules from the module folder")
    parser.add_argument('-d','--debug', action= 'store_true', default= False, dest= 'debug_switch', help = "Modify program executing to start the debug-path")
    args = parser.parse_args()
    
    # Print fancy logo lmaoo
    print(logo_string)
    
    # Start the main loop
    main_loop(module_switch = args.module_switch)

if __name__ == "__main__":
    main()
