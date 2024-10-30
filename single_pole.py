import numpy as np
import matplotlib.pyplot as plt

# Get the pole from user input
pole_input = input("Enter the pole (e.g., -1+2j): ")
pole = complex(pole_input)

# Define the frequency range
w = np.linspace(-10, 10, 1000)

# Calculate H(w) based on the pole
H_w = 1 / (1 - 1j * w / pole)

# Calculate magnitude and phase
magnitude_H = np.abs(H_w)
phase_H = np.angle(H_w)

# Plotting
plt.figure(figsize=(12, 8))

# Magnitude plot
plt.subplot(2, 1, 1)
plt.plot(w, magnitude_H, 'b')
plt.title('Magnitude of H(w)')
plt.xlabel('Frequency (w)')
plt.ylabel('|H(w)|')
plt.grid()

# Phase plot
plt.subplot(2, 1, 2)
plt.plot(w, phase_H, 'r')
plt.title('Phase of H(w)')
plt.xlabel('Frequency (w)')
plt.ylabel('Phase of H(w) (radians)')
plt.grid()

plt.tight_layout()
plt.show()
