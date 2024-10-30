import numpy as np
import matplotlib.pyplot as plt

# Get the number of poles
num_poles = int(input("Enter the number of poles: "))
poles = []

# Collect poles from user input
for i in range(num_poles):
    pole_input = input(f"Enter pole {i + 1} (e.g., -1+2j): ")
    poles.append(complex(pole_input))

# Define the frequency range
w = np.linspace(-10, 10, 1000)

# Calculate H(w) based on the poles
H_w = np.prod([(1 - 1j * w / p) for p in poles], axis=0)

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
