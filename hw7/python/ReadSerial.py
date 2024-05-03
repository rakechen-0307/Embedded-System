import serial
import time
import csv
import struct
from collections import deque
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = open("serial.in", "w")
f.write('')
f.close()

data_limit = 500
csv_file = 'data.csv'
fieldnames = ["timestamp", "x", "y", "z",
              "x_filtered", "y_filtered", "z_filtered"]
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

start_time = time.time()
ser = serial.Serial('COM6', 115200, timeout=1000)


def receive_msg():
    timestamp = 0
    while (True):
        data = ser.readline()
        if (data):
            values = data.split()
            if len(values) == 3:
                print(
                    f"timestamp: {timestamp}, x: {int(values[0])}, y: {int(values[1])}, z: {int(values[2])}")
                timestamp += 1
                with open('data.csv', 'a') as csv_file:
                    csv_writer = csv.DictWriter(
                        csv_file, fieldnames=fieldnames)
                    csv_writer.writerow(
                        {"timestamp": timestamp, "x": int(values[0]), "y": int(values[1]), "z": int(values[2])})


def receive_byte():
    while (True):
        data = ser.read_all()
        if (data):
            # write the data to serial.in
            # print(' '.join(f'{byte:02X}' for byte in data))
            with open("serial.in", "a") as f:
                f.write(' ')
                f.write(' '.join(f'{byte:02X}' for byte in data))


def raw_to_csv():
    timestamp = 0
    with open('serial.in', 'r') as f:
        raw_data = f.read().split()
    for i in range(0, len(raw_data), 2):
        byte1 = raw_data[i]
        byte2 = raw_data[i+1]
        value = (byte1 << 8) | byte2
        print(f"int: {value}")

        # write the data to csv
        with open('data.csv', 'a') as cfile:
            csv_writer = csv.DictWriter(
                cfile, fieldnames=fieldnames)

            info = {
                "timestamp": timestamp,
                "value": value,
            }

            csv_writer.writerow(info)
            timestamp += 1


def receive_float():

    # receive for timeout seconds
    loop_timeout = 5
    while (time.time() - start_time) < loop_timeout:
        data = ser.read_all()
        if (data):
            print(' '.join(f'{byte:02X}' for byte in data))
            with open("serial.in", "a") as f:
                f.write(' ')
                f.write(' '.join(f'{byte:02X}' for byte in data))

    # process the data from byte to float
    with open('serial.in', 'r') as f:
        raw_data = f.read().split()

    start_index = []
    for i in range(0, len(raw_data), 1):
        sequence = get_starter("start")
        if str(sequence[0]) == str(raw_data[i]) and str(sequence[1]) == str(raw_data[i+1]) and str(sequence[2]) == str(raw_data[i+2]) and str(sequence[3]) == str(raw_data[i+3]) and str(sequence[4]) == str(raw_data[i+4]):
            print("Sequence found!")
            start_index.append(i+5)

    for i in range(0, len(start_index), 1):
        print(f"Start index: {start_index[i]}")

    converted_unfiltered_data = []
    converted_filtered_data = []
    for j in start_index[:-1]:
        for i in range(j, j+320*4, 4):
            byte1 = int(raw_data[i], 16)
            byte2 = int(raw_data[i+1], 16)
            byte3 = int(raw_data[i+2], 16)
            byte4 = int(raw_data[i+3], 16)
            float_value = struct.unpack('f', struct.pack(
                'BBBB', byte1, byte2, byte3, byte4))[0]
            converted_unfiltered_data.append(float_value)

        for i in range(j+320*4, j+320*4*2, 4):
            byte1 = int(raw_data[i], 16)
            byte2 = int(raw_data[i+1], 16)
            byte3 = int(raw_data[i+2], 16)
            byte4 = int(raw_data[i+3], 16)
            float_value = struct.unpack('f', struct.pack(
                'BBBB', byte1, byte2, byte3, byte4))[0]
            converted_filtered_data.append(float_value)

    # write the data to csv
    timestamp = 0
    for i in range(0, (len(start_index)-1)*320, 1):
        with open('data.csv', 'a') as cfile:
            csv_writer = csv.DictWriter(
                cfile, fieldnames=fieldnames)

            info = {
                "timestamp": timestamp,
                "x": converted_unfiltered_data[i],
                "x_filtered": converted_filtered_data[i],
            }

            csv_writer.writerow(info)
            timestamp += 1


def get_starter(starter: str) -> list[str]:
    converted_start = ' '.join(f'{ord(c):02X}' for c in starter)
    converted_start = converted_start.replace('0x', '')
    int_array = [int(num) for num in converted_start.split()]
    converted_start = converted_start.split()
    return int_array


receive_float()
ser.close()


csv_file = 'data.csv'
plt.style.use('fivethirtyeight')
data = pd.read_csv(csv_file)
t_vals = data['timestamp']
x_vals = data['x']
x_filtered_vals = data['x_filtered']

plt.cla()

plt.plot(t_vals, x_vals, label='x')
plt.plot(t_vals, x_filtered_vals, label='x_filtered')

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
