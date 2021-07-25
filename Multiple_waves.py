# Importing all the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Constructing a Time Doamin Audio Signal
Fs = 2000     # This is the sampling frequency
tstep = 1/Fs  # This is the time interval of the Audio Signal
f0 = 100      # Taking Ideal Sine Signal with 100Hz frequency

N = int(10*Fs/f0)  # No. of Samples of Signal
# Using the NumPy Libra
# try to Generate Data Points for sine wave
# total time steps of the timme domain signal
t = np.linspace(0, (N-1)*tstep, N)
fstep = Fs/N                       # frequency interval
f = np.linspace(0, (N-1)*fstep, N)  # freq steps

# Generating Sine Wave using Numpy Library
y = 1*np.sin(2*np.pi*f0*t) + 2*np.sin(2*np.pi*2*f0*t)
# using fft
X = np.fft.fft(y)
X_mag = np.abs(X)/N
f_plot = f[0:int(N/2+1)]
X_mag_plot = 2*X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0]/2


# plotting the graph using matplot Library
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_mag_plot, '.-')

plt.show()
