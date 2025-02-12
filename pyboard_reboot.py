#!/usr/bin/env python3
from uploader_functions.uploader_functions import *


if __name__ == "__main__":
    argv = sys.argv
    SystemHeader = PrintSystemHeader()
    PyboardHeaderString = PrintPyboardHeader()


    argv_list = ['-help', '-h', '-port', '-p']

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
            print_like_GPT('python3 pyboard_reboot.py [-h|-help]\n\n', bcolors.color256(fg=229))

            print_like_GPT('Example2. To upload programs to your /pyboard:\n', bcolors.color256(fg=229))
            print_like_GPT('python3 pyboard_reboot.py [-p|-port] /port_to_pyboard\n', bcolors.color256(fg=229))
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

        else:
            print_like_GPT(SystemHeader + 'Invalid arguments\n', bcolors.FAIL)
            os._exit(0)


    pyboard_soft_reset(port)
    os.system('clear')
    print_like_GPT(PyboardHeaderString + "System rebooted.\n\n", bcolors.FAIL)
    print_like_GPT(".DAYDAWNDREAM Studio 2025.\n\n", bcolors.color256(fg=224))