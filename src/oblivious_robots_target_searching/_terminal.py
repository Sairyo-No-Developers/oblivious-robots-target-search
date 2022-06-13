from . import Graph
from ._version import __version__


def run():
    print(f"Oblivious Robots Target Search Version : {__version__}")
    P = Graph.Playground(False)
    P.setup()
    P.run()
    
def terminal(args):
    if len(args) == 0:
        run()
        exit()
    
    if args[0] in ['-h', '--help']:
        print(f"Oblivious Robots Target Searching")
        print("------------------------------------")
        print("Running it without any arguments, defaults to sim=False, i.e., the interactive way.")
        print("")
        print("[Arguments]")
        print("-v, --version : Outputs the current version of the package installed.")
        print("-h, --help : Outputs the help guide on how to use the package.")
        print("")
        print("Thanks!")
        exit()  
    
    if args[0] in ['-v', '--version']:
        print(f"version {__version__}")
        exit()    

    print("Please check the arguments. Pass -h or --help for more info.")
    exit()
