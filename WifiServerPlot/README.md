# Embedded System HW2 (Group 8)

This is the server code for receiving sensor data from STM32 iot node

## How to use

Set the ipv4 address of the server in the file `server.py` at line 10

```python
HOST = "Your IPv4 address"  # IP address
```

and on line 31 of `main.cpp`

```c++
#define HOSTNAME "IPv4 address of server"
```

start the server program by running the following command on the server PC

```bash
python .\server.py
```

Start the client program by running `main.cpp` in mbed OS on the STM32 iot node

After the server is started, the server will listen to the port 8000 and wait for the sensor data from the STM32 iot node.

### Plot

Run the following command to plot the sensor data on server PC

```bash
python .\plot.py
```
