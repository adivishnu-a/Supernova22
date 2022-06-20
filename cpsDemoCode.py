import msvcrt
import random
import time
import sys
import os


#DOCUMENTATION:
#This is a Python program that demonstrates the process that happens during Cellular Payment Service
#Project on Behalf of Team CODEJAMS
#By Adi Vishnu Avula

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def message(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)


def load(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.5)

#main
os.system('cls')

#Step 1 - Dialing
time.sleep(0.1)
msg1_1 = f"{bcolors.BOLD}User "+f"{bcolors.CYAN}"+str(random.randrange(8248, 9948, 4))+"######"+f"{bcolors.ENDC}"
message(msg1_1)
msg1_2 = f"{bcolors.BOLD} is connected to Cellular Payment Service via Toll-Free number{bcolors.ENDC}"
message(msg1_2)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 2 - Language Preference
msg2_1 = "<Announcing the Language options> : "
message(msg2_1)
time.sleep(1.5)
msg2_2 = f"{bcolors.YELLOW}User selected Language "+str(random.randrange(1, 4, 1))+f"{bcolors.ENDC}"
message(msg2_2)
time.sleep(0.3)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 3 - PIN
msg3_1 = "<Prompting the user to enter the PIN number> : "
message(msg3_1)
msg3_2 = f"{bcolors.RED}******{bcolors.ENDC}"
load(msg3_2)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 4 - Amount to be transferred
msg4_1 = "<Announcing the remaining balance in user account>"
message(msg4_1)
time.sleep(1.6)
print("")
msg4_2 = "<Prompting the user to enter the amount to transfer> : "+f"{bcolors.BLUE}Rs. "
message(msg4_2)
msg4_3 = str(random.randrange(100, 2000, 50))+f"{bcolors.ENDC}"
load(msg4_3)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 5 - Recipient Information
msg5_1 = "<The user is entering the phone number of the recipient> : "
message(msg5_1)
msg5_2 = f"{bcolors.CYAN}"+str(random.randrange(8248, 9948, 4))+"######"+f"{bcolors.ENDC}"
load(msg5_2)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 6 - Confirmation
msg6_1 = "<Asking for final confirmation from the user>"
message(msg6_1)
time.sleep(0.5)
print("")
msg6_2 = "<1 to PROCEED and 2 to CANCEL> : "
message(msg6_2)
msg6_3 = f"{bcolors.GREEN}"+str(1)+f"{bcolors.ENDC}"
message(msg6_3)
print("")
load("...")
print("")
time.sleep(0.4)

#Step 7 - Transaction
msg7_1 = "Processing Transaction"
message(msg7_1)
print("")
time.sleep(0.2)
load("...")
print("")
msg7_2 = f"{bcolors.BOLD}TRANSACTION SUCCESSFUL{bcolors.ENDC}"
message(msg7_2)
print("")
time.sleep(0.2)
msg7_3 = f"{bcolors.GREEN}---Confirmation SMS sent to User---{bcolors.ENDC}"
message(msg7_3)
print("")

msvcrt.getch()
