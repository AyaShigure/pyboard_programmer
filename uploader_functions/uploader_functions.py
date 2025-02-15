from .bcolors import *
import datetime
import time
import pyfiglet
import serial
import os
import sys
version_number = 0.2 # MMXXV-II-XV, a few days after the inverview with FANUC corporation.

''' MMXXV-II-XV, Aya Wang:
    IMPORTANT:
        This function set is for Linux/MacOS hosts device to upload code under /pico_src to RP2040 or other MCUs with Micropython firmware.
        Do not upload this file to /pyboard.
'''

def fancy_print():
    ascii_art = pyfiglet.figlet_format("DAYDAWNDREAM", font="big", width = 100)
    print_like_GPT(ascii_art)
    print_like_GPT('/*******************************************/\n', bcolors.OKCYAN)
    print_like_GPT('  A Micropython file system syncing tool\n', bcolors.OKCYAN)
    print_like_GPT('       for RP2040/ESP series MCUs.\n', bcolors.OKCYAN)
    print_like_GPT(f'     ...MMXXV-II-XII...Version {version_number}...\n', bcolors.OKCYAN)
    print_like_GPT('  Created by Aya Wang, DAYDAWNDREAM Studio.\n', bcolors.OKCYAN)
    print_like_GPT('/*******************************************/\n\n', bcolors.OKCYAN)


# Utilities
def PrintPyboardHeader(default_print = False):
    headerString = '[' + 'Pyboard' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    if default_print:
        print_like_GPT(headerString + 'Initiallizing\n', bcolors.color256(fg=154))
    return headerString


def PrintAyaWangHeader(default_print = False):
    headerString = '[' + 'Aya Wang' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    if default_print:
        print_like_GPT(headerString + 'Initiallizing\n', bcolors.color256(fg=210))
    return headerString

def PrintSystemHeader(default_print = False):
    headerString = '[' + 'System' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    if default_print:
        print_like_GPT(headerString + 'Initiallizing\n', bcolors.FAIL)
    return headerString

def PrintMBPM4Header(default_print = False):
    headerString = '[' + 'MacBook Pro - M4' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    if default_print:
        print_like_GPT(headerString + 'Initiallizing\n', bcolors.color256(fg=193))
    return headerString

def print_like_GPT(text, color=bcolors.ENDC):
    for i,char in enumerate(text):
        print(f"{color}{char}\u2588{bcolors.ENDC}", end="", flush=True)
        time.sleep(0.0005)

        if i < len(text) - 1:
            print('\b \b', end='', flush=True)
    time.sleep(0.001) 

    print('\b \b', end='', flush=True) 

def pyboard_soft_reset(port):
    os.system(f"rshell -p {port} 'repl ~ import machine ~ machine.soft_reset() ~'")

def active_serial_monitor(port, headerString):
    SystemHeader = PrintSystemHeader()
    print_like_GPT(SystemHeader + 'Activating the serial monitor...\n', bcolors.FAIL)
    time.sleep(1)
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        os.system("clear")
        fancy_print()

    except serial.serialutil.SerialException:
        print_like_GPT(SystemHeader + 'PortError: Invalid Port\n', bcolors.FAIL)
        os._exit(0)

    print_like_GPT(headerString + "Ready...\n\n",bcolors.WARNING)

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print_like_GPT(headerString + f"{line}\n",  bcolors.color256(fg=154))
            # ser.flushInput()
            time.sleep(0.1)

    except KeyboardInterrupt:
        print_like_GPT(SystemHeader + 'KeyboardInterrupt, exiting.', bcolors.FAIL)
    finally:
        ser.close()