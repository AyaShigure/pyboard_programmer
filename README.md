# Pyboard Embedded Software Tool

## Known Bug: MMXXV-II-XII

- **Issue:**
  When a valid port path is provided, the rshell returns a fail message.
  Despite this, the program continues running and ultimately returns the message ALL NORMAL.

- **Workaround:**
  Ensure that the port passed in is correct.

---

## Execution Tip

To execute a Python script directly from the terminal, mark it as executable:

`chmod +x xxx.py` 


---

## pyboard_sync.py

### Usage 1: Display Help

`python3 pyboard_sync.py -h`

### Usage 2: Upload Programs and Reboot

- **Description:**
  This command uploads all programs under the /pico_src directory.
  Once the upload is complete, the pyboard is automatically rebooted.
  After the first reboot, the pyboard will execute main.py.

- **Command:**

`python3 pyboard_sync.py -p /port_to_pyboard`

### Usage 3: Upload Programs and Activate Serial Monitor

- **Description:**
  This command uploads all programs under /pico_src and then activates the serial monitor.

- **Command:**

`python3 pyboard_sync.py -p /port_to_pyboard -sm`

---

## pyboard_sm.py

### Usage 1: Display Help

`python3 pyboard_sm.py -h`

### Usage 2: Activate Serial Monitor

- **Description:**
  Activates the serial monitor for the specified pyboard.

- **Command:**

`python3 pyboard_sm.py -p /port_to_pyboard`

---

## pyboard_reboot.py

### Usage 1: Display Help

`python3 pyboard_reboot.py -h`

### Usage 2: Reboot the Pyboard

- **Description:**
  Reboots the pyboard connected to the specified port.

- **Command:**

`python3 pyboard_reboot.py -p /port_to_pyboard`