#!/usr/bin/env python3
from uploader_functions.uploader_functions import *

if __name__ == '__main__':
    SystemHeader = PrintSystemHeader()
    argv = sys.argv
    argv_list = ['-help', '-h', '-port', '-p']

    if  len(argv) == 1 or len(argv) > 3:
        print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
        os._exit(0)

    elif argv[1] not in argv_list:
        print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
        os._exit(0)

    else:
        if argv[1] in argv_list[0:2]:
            # help

            print_like_GPT('/*************************************************************/\n', bcolors.OKCYAN)
            print_like_GPT('Example1. To show this help:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 sm.py [-h|-help]\n\n', bcolors.color256(fg=229))

            print_like_GPT('Example2. To activate the serial monitor to /pyboard:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 sm.py [-p|-port] /port_to_pyboard\n', bcolors.color256(fg=229))
            print_like_GPT('/*************************************************************/\n', bcolors.OKCYAN)
            os._exit(0)
   
        elif argv[1] in argv_list[2:4]:
            # port
            if len(argv) != 3 :
                print_like_GPT(SystemHeader + 'No port is provided\n', bcolors.FAIL)
                os._exit(0)
            else:
                port = argv[2]
        else:
            print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
            os._exit(0)


    # port = '/dev/ttyACM0'    # Under Linux
    PyboardHeaderString = PrintPyboardHeader(default_print=True)
    SystemHeader = PrintSystemHeader(default_print=True)
    print_like_GPT(SystemHeader + f'Attaching serial monitor to port: {port}.\n', bcolors.color256(fg=229))

    active_serial_monitor(port, PyboardHeaderString)

    