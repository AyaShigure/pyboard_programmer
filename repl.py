#!/usr/bin/env python3
from uploader_functions.uploader_functions import *

'''
    Directly activate repl to /pyboard via rshell 
'''

if __name__ == '__main__':
    SystemHeader = PrintSystemHeader()
    argv = sys.argv
    argv_list = ['-help', '-h', '-port', '-p']
    auto_mode = False

    if len(argv) == 1:
        print_like_GPT(SystemHeader + 'Automatically connecting to /pyboard...\n', bcolors.color256(fg=229))
        auto_mode = True

    elif len(argv) > 3:
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
            print_like_GPT('python3 repl.py [-h|-help]\n\n', bcolors.color256(fg=229))

            print_like_GPT('Example2. To activate the serial monitor to /pyboard:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 repl.py [-p|-port] /port_to_pyboard\n', bcolors.color256(fg=229))
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

    print_like_GPT(PyboardHeaderString + 'Connecting to the pyboard...\n', bcolors.color256(fg=229))

    os.system('clear')
    fancy_print()
    if auto_mode:
        os.system(f"rshell 'repl'")
    else: 
        os.system(f"rshell -p {port} 'repl'")