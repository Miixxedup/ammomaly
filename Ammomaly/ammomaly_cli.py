import argparse
from Ammomaly.ammomaly_core.loop import *
from Ammomaly.assets.logo import logo_string
from Ammomaly.utils.logger import *

def main():    
    
    parser = argparse.ArgumentParser('Ammomaly framework to handle sudden changes in an environment')
    parser.add_argument('-m','--modules', action= 'store_true', default= False, dest= 'module_switch', help= "Start ammomaly with all .py modules from the module folder")
    parser.add_argument('-d', '--debug', help="Be debug", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING,)
    parser.add_argument('-v', '--verbose',help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO)    
    
    args = parser.parse_args()
    print(args)
    
    # Apply log level
    logging.basicConfig(level=args.loglevel)
    
    # Print fancy logo lmaoo
    print(logo_string)
    
    # Start the main loop
    main_loop(module_switch = args.module_switch)

if __name__ == "__main__":
    main()
