from datetime import datetime
import config
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)




from config import *

if ALIVE_PIC:
    ALIVE_PIC = ALIVE_PIC
else: 
    ALIVE_PIC = "https://telegra.ph/file/291e92e0df0d1edefc516.jpg"

if not STRING1:
    logging.error("At least 1 string is required! Exiting!")
    quit(1)

if API_ID:
    API_ID = API_ID
else:
     API_ID = 10248430
    

if API_HASH:
    API_HASH = API_HASH
else:
     API_HASH = 42396a6ff14a569b9d59931643897d0d
    

if STRING1:
    print("[INFO] STRING1 Found!! Booting Dangi userbot Client1... ") 
    bot1 = Client(session_name=STRING1, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot1 = None

if STRING2:
    print("[INFO] STRING2 Found!! Booting Bot Client1... ") 
    bot2 = Client(session_name=STRING2, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot2 = None

if STRING3:
    print("[INFO] STRING3 Found!! Booting mBot Client1... ") 
    bot3 = Client(session_name=STRING3, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot3 = None

if STRING4:
    print("[INFO] STRING4 Found!! Booting Bot Client1... ") 
    bot4 = Client(session_name=STRING4, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot4 = None

if STRING5:
    print("[INFO] STRING5 Found!! Booting SpamBot Client1... ") 
    bot5 = Client(session_name=STRING5, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot5 = None
    
if STRING6:
    print("[INFO] STRING6 Found!! Booting Bot Client1... ") 
    bot6 = Client(session_name=STRING6, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f""))
else:
    bot6 = None
    
if STRING7:
    print("[INFO] STRING7 Found!! Booting Bot Client7... ") 
    bot7 = Client(session_name=STRING7, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot7 = None
    
if STRING8:
    print("[INFO] STRING8 Found!! Booting Bot Client8... ") 
    bot8 = Client(session_name=STRING8, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot8 = None
    
if STRING9:
    print("[INFO] STRING9 Found!! Booting Bot Client9... ") 
    bot9 = Client(session_name=STRING9, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot9 = None

if STRING10:
    print("[INFO] STRING10 Found!! Booting SpamBot Client10... ") 
    bot10 = Client(session_name=STRING10, api_id=API_ID, api_hash=API_HASH, plugins=dict(root=f"DEADLY.plugins"))
else:
    bot10 = None

scheduler = AsyncIOScheduler()
START_TIME = datetime.now()
