from scipy import signal
numtaps = 28
f = 0.05
coeffs = signal.firwin(numtaps, f)

for coff in coeffs:
    print(coff, end='f, ')
