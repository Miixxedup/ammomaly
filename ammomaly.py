from main import *
import argparse

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

