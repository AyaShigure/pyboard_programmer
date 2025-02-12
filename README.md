# Pyboard embedded software tool

Tip:
Use `chmod +x xxx.py` to directely execute with `./xxxx.py` from terminal.


# pyboard_sync.py
Usage 1: 
### Call for help.
`python3 pyboard_sync.py -h`

Usage 2: 
### Upload all programs under /pico_src, pyboard will be rebooted once this is done. Then the pyboard will execute main.py after first reboot.
`python3 pyboard_sync.py -p /port_to_pybord`

Usage 3: 
### Upload all programs under /pico_src, then activate the serial monitor.
`python3 pyboard_sync.py -p /port_to_pybord -sm`

# pyboard_sync.py
Usage 1: 
### Call for help.
`python3 pyboard_sm.py -h`

Usage 2: 
### Activate the serial monitor.
`python3 pyboard_sm.py -h`