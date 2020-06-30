import time
import psutil
import os
import sys

#-----------------Network usage---------------------
def network_usage_shutdown():
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_gbit(value):
    return value/1024./1024./1024.*8

def send_stat(value):
    mbs = (convert_to_gbit(value))*1000
    print(mbs, "mbs")
    if mbs == 0:
        os.system("shutdown -s -t 30")
        sys.exit()
#-----------------------------------------------------


#------------------timed-------------------------       
def timed_shutdown():
    userInput = int(input("Enter minutes: "))
    minutes2seconds = str(userInput * 60)
    os.system("shutdown -s -t " + minutes2seconds)
#-----------------------------------------------------

    
def main():
    print("How would you like to schedule your shutdown?")
    print("1. Using network usage")
    print("2. Using time")
    userChoice = int(input("---> "))
    if userChoice == 1:
        network_usage_shutdown()
    elif userChoice == 2:
        timed_shutdown()


main()
