from sibase.SIApi import SIApi as api
from sibase.SICore import SICore as core
from sibase.Config import Config
import os





def main():
    si = core()
    os.system('cls')

    print(si.MaskValue("Jimmi"))

    
    

if __name__ == "__main__":
    main()