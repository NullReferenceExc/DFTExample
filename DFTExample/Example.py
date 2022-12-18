import DFT
import Graphics
import math

SF = 100
T = 5

dft = DFT.DFT(F = lambda x: math.sin(math.pi * 2 * 45 * x), T = T, SF = SF)

complex_amplitudes: list = dft.calculate()
amplitudes, phases = {}, {}
for ca in complex_amplitudes:
    if ca.freq >= 0:
        amplitudes.update({ca.freq: ca.amplitude})
        phases.update({ca.freq: ca.phase})

Graphics.show_dict_on_graphic("Amplitudes", "Frequency", "Amplitude", amplitudes, False)
Graphics.show_dict_on_graphic("Phases", "Frequency", "Phase", phases, True)
