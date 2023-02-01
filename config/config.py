import os

import re
import sys
from os import getenv
from resources.data import DEV
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




API_ID = int(getenv("API_ID", "24007062"))
API_HASH = getenv("API_HASH", "6bc45ea5ad704f9de7c772e2dbf93d00")
ALIVE_PIC = getenv("ALIVE_PIC", None)

#CLIENT SESSION

STRING1 = getenv("STRING_SESSION", "BQBZIob_3EVhoPBlvONNlcSYmZMkKnbHk0tHMuV0hgw1GYZol3JK7ZZLupdxpQKlItX87RAHIrMsxmpvhlSyCBmgdXaBgFSBSIzly2NFWlwzqKyGucI5rYBC9E7QhcR5BlClouDeGAhkyWV6sHw41mEioB63GWrdsI5yxU6NJd6kL6i7hM3Ly9j7oZADWHaRrOMtfCVUuoqfJItZwuwgbBSAbBVslRqf8i6DCC28SdPf-WmXjjiZsD4id6H36T5Egcbzp0gd-G43mKtkhy38sSEhfCGXkct-Y1yZmvjbShlo3tgpC-w7T8Pd3_2mOMmFdPNVYLiI6DSFcn21uq9DEv0lAAAAAUhO7k4A" )
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)
OWNER_ID = int(getenv("OWNER_ID", "5508099662")) 
SUDO_USERS = getenv("SUDO_USER", "5508099662") 


"""
------------------------------DON'T EDIT AFTER THIS LINE---------------------------------------
"""

# CONVERTING STR TO INT

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list




# SUDO SETUP

SUDOERS = []

if SUDO_USERS:
    SUDOERS = make_int(SUDO_USERS)

DEVS = DEV
for i in DEVS:
    SUDOERS.append(i)
    SUDOERS.append(OWNER_ID)
