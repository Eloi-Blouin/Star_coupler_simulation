import numpy as np
import matplotlib.pyplot as plt


def fsr_nm(wavelength_nm):
	"""Return FSR in nm using FSR = lambda^2 / (2.05*300), with lambda in um."""
	c = 2.05 * 300
	wavelength_um = np.asarray(wavelength_nm) * 1e-3
	fsr_um = wavelength_um**2 / c
	return fsr_um * 1e3


def main() -> None:
	# Wavelength axis (nm)
	wavelength_nm = np.linspace(1550.0, 1560.0, 3000)
	wavelength_um = wavelength_nm * 1e-3

	# Constant from FSR formula
	c = 2.05 * 300

	# Integrated phase so local period follows FSR(lambda)
	# d(theta)/d(lambda_um) = 2*pi / FSR_um(lambda_um) = 2*pi*c / lambda_um^2
	lambda0_um = 1.55
	theta_base = 2.0 * np.pi * c * (1.0 / lambda0_um - 1.0 / wavelength_um)

	phase_offsets = [0.0, np.pi / 4.0, np.pi/2, 3*np.pi/4 ]
	labels = ["phi = 0", "phi = π/4", "phi = π/2", "phi = 3π/4"]
	colors = ['red', 'blue', 'green', 'orange']

	plt.figure(figsize=(8, 6))
	for phi, label, color in zip(phase_offsets, labels, colors):
		transmission = 0.5 * (1.0 + np.cos(theta_base + phi))
		plt.plot(wavelength_nm, transmission, color=color, lw=1.6, label=label)

	plt.xlim(min(wavelength_nm), max(wavelength_nm))
	plt.ylim(0, 1.02)
	plt.xlabel("Wavelength (nm)", fontsize=16)
	plt.ylabel("Transmission (normalized)", fontsize=16)
	plt.legend(loc="upper right", fontsize=12, frameon=True)
	plt.tick_params(direction="in", top=True, right=True, width=1.0, labelsize=13)
	plt.tight_layout()
	plt.show()

	fsr_1550 = float(fsr_nm(1550.0))
	print(f"FSR at 1550 nm = {fsr_1550:.3f} nm")


if __name__ == "__main__":
	main()

