from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

numtaps = 28
f = 0.05
coeffs = signal.firwin(numtaps, f)

for coff in coeffs:
    print(coff, end='f, ')

# Compute the frequency response
w, h = signal.freqz(coeffs, 1)

# Plot the magnitude response
plt.figure()
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response')
plt.xlabel('Frequency [radians / sample]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.show()

# Define the time vector t
t = np.arange(0, 320)
x = np.sin(2*np.pi*0.008*t)
output = signal.lfilter(coeffs, 1, x)
np.savetxt('filtered_output.csv', output, delimiter=',')

# Plot the original and filtered signals
plt.figure()
plt.plot(t, x, label='Original Signal')
plt.plot(t, output, label='Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original and Filtered Signals')
plt.legend()
plt.grid(True)
plt.show()