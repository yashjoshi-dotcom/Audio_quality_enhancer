# Importing all the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Constructing a Time Doamin Audio Signal
Fs = 2000     # This is the sampling frequency
tstep = 1/Fs  # This is the time interval of the Audio Signal
f0 = 100      # Taking Ideal Sine Signal with 100Hz frequency

N = int(Fs/f0)  # No. of Samples of Signal
# Using the NumPy Libra
# try to Generate Data Points for sine wave
# total time steps of the timme domain signal
t = np.linspace(0, (N-1)*tstep, N)
fstep = Fs/N                       # frequency interval
f = np.linspace(0, (N-1)*tstep, N)  # freq steps

# Generating Sine Wave using Numpy Library
y = 1*np.sin(2*np.pi*f0*t)

# plotting the graph using matplot Library
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t, y, '.-')
plt.show()
