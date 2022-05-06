import numpy as np
import scipy.constants as constants

def range(P, G, wavelength, RCS, SNR, k, T, B, F, Ls):
    R4 = P*G**2 *wavelength**2*RCS/((4*np.pi)**3*SNR*k*T*B*F*Ls)
    return pow(R4, 0.25)

def dB2lin(x):
    return pow(10, x/10)

print(range(1,1,1,1,1,1,constants.Boltzmann,1,1,1))

print("3dB is : ", dB2lin(3))
print("-3dB is : ", dB2lin(-3))

print(range(1, dB2lin(28), 3000e6, 1, dB2lin(20), constants.Boltzmann, 290, 1, 1, dB2lin(1)))
