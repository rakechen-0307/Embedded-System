#!/usr/bin/env python3
import socket
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from itertools import count
from matplotlib.animation import FuncAnimation

HOST = "Your IPv4 address"  # IP address
PORT = 8000  # Port to listen on (use ports > 1023)

# Path to your CSV file
csv_file = 'data.csv'
fieldnames = ["timestamp", "value"]
timestamp = 0

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# Server
print('Starting server')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)

            # Assuming data format is "timestamp,value"
            value = data
            with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                info = {
                    "timestamp": timestamp,
                    "value": value,
                }

                timestamp += 1
                csv_writer.writerow(info)
                print(timestamp, value)
