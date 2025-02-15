#!/usr/bin/env python3
from uploader_functions.uploader_functions import *

'''
    1. Delete all files on pico
    2. Sync the file trees from local to pico (main.py and the ./includes)
    3. Active 
'''

''' 2025-2-12
    Todo: Add a workspace initialization routine 
        Initialize /pico_src
        Initialize ./upload.py 
        Etc.

    Known bug:
        When input a valid port path, the rshell will return fail, but the porgram keeps going and returns ALL NORMAL.
        For now just MAKE SURE the port passed in is correct.
'''

if __name__ == "__main__":
    argv = sys.argv
    activate_serial_monitor = False
    SystemHeader = PrintSystemHeader()
    PyboardHeaderString = PrintPyboardHeader()


    argv_list = ['-help', '-h', '-port', '-p', '-sm'] # -sm should always be the last one

    if  len(argv) > 4 or len(argv) < 2:
        print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
        os._exit(0)

    elif argv[1] not in argv_list[0:4]:
        print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
        os._exit(0)

    else:
        if argv[1] in argv_list[0:2]:
            # help
            print_like_GPT('/*************************************************************/\n', bcolors.OKCYAN)
            print_like_GPT('Example1. To show this help:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 sync.py [-h|-help]\n\n', bcolors.color256(fg=229))

            print_like_GPT('Example2. To upload programs to your /pyboard:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 sync.py [-p|-port] /port_to_pyboard\n\n', bcolors.color256(fg=229))

            print_like_GPT('Example3. To upload and monitor the serial port:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 sync.py [-p|-h] /port_to_pyboard -sm\n', bcolors.color256(fg=229))
            print_like_GPT('/*************************************************************/\n', bcolors.OKCYAN)

            os._exit(0)
   
        elif argv[1] in argv_list[2:4]:
            # port
            if len(argv) < 3:
                print_like_GPT(SystemHeader + 'No port is provided\n', bcolors.FAIL)
                os._exit(0)
            else:
                port = argv[2]
                if not os.path.exists(port):
                    print_like_GPT(SystemHeader + f'Error: Port {port} does not exist. Please check the connection.', bcolors.FAIL)
                    os._exit(0)
                if argv[-1] == '-sm':
                    activate_serial_monitor = True
        else:
            print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
            os._exit(0)

    os.system("clear")
    # Upload via rshell
    try:
        fancy_print()
        print_like_GPT(PyboardHeaderString + 'Clearing the existing file tree.\n', bcolors.color256(fg=229))
        os.system(f"rshell -p {port} rm -r /pyboard/*")
        print_like_GPT(PyboardHeaderString + 'Uploading the new file tree.\n', bcolors.color256(fg=229))
        os.system(f"rshell -p {port} rsync ./pico_src/ /pyboard/")
        print_like_GPT(PyboardHeaderString + "Done............\n", bcolors.color256(fg=229))
        print('\n\n')
        print_like_GPT(PyboardHeaderString + "REBOOTING THE MCU NOW.......\n", bcolors.FAIL)
        print('\n\n')

        # MCU soft reboot
        # time.sleep(2)
        pyboard_soft_reset(port)
        os.system('clear')
        print_like_GPT(PyboardHeaderString + "Embedded system is updated.\n", bcolors.FAIL)
        print_like_GPT(PyboardHeaderString + "System rebooted.\n\n", bcolors.FAIL)
        print_like_GPT(" .DAYDAWNDREAM Studio 2025.\n\n", bcolors.color256(fg=224))

    except Exception as e:
        print_like_GPT(SystemHeader + "Unable to upload. Please check the serial port/connection.\n", bcolors.FAIL)
        os._exit(0)

    if activate_serial_monitor:
        os.system("clear")
        PyboardHeaderString = PrintPyboardHeader()
        active_serial_monitor(port, PyboardHeaderString)
