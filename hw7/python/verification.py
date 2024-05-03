import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the ideal filtered data
filtered_output = np.loadtxt('filtered_output.csv', delimiter=',')

# read the real filtered data

csv_file = 'data.csv'
data = pd.read_csv(csv_file)

t = data['timestamp'][:320]
x = data['x'][:320]
x_filtered_vals = data['x_filtered'][:320]

# Plot the original and filtered signals
plt.figure()
plt.plot(t, x, label='Original Signal: sin(2pi*0.008*t)')
plt.plot(t, x_filtered_vals, label='Filtered Signal by STM32')
plt.plot(t, filtered_output, label='Ideal Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Verification of the correctness of the implementation by filtering a sine wave')
plt.legend()
plt.grid(True)
plt.show()