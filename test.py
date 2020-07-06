from sibase.SIApi import SIApi as api
from sibase.SICore import SICore as core
from sibase.Config import *

si = core()



print(GetConfigValue("api", "port"))