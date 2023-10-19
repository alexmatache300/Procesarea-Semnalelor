#1

import numpy as np
import matplotlib.pyplot as plt

amplitudine = 2.0
frecventa = 1.0
faza = np.pi/4

timp = np.linspace(0, 2, num=1000)

semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)

semnal_cosinus = amplitudine * np.cos(2 * np.pi * frecventa * timp + faza)

plt.figure(figsize=(10, 6))

plt.subplot(211)
plt.plot(timp, semnal_sinus, label='Semnal Sinusoidal')
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Sinusoidal')
plt.grid()
plt.legend()

plt.subplot(212)
plt.plot(timp, semnal_cosinus, label='Semnal Cosinusoidal')
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Cosinusoidal')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


#4

import numpy as np
import matplotlib.pyplot as plt

amplitudine_sinus = 1.0
frecventa_sinus = 2.0
faza_sinus = 0.0

amplitudine_sawtooth = 0.5
frecventa_sawtooth = 1.0
durata_sawtooth = 1.0

timp = np.linspace(0, 5, num=1000)

semnal_sinus = amplitudine_sinus * np.sin(2 * np.pi * frecventa_sinus * timp + faza_sinus)

semnal_sawtooth = amplitudine_sawtooth * np.mod(timp, durata_sawtooth) / durata_sawtooth

suma_semna = semnal_sinus + semnal_sawtooth

plt.figure(figsize=(12, 8))

plt.subplot(311)
plt.plot(timp, semnal_sinus)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Sinusoidal')
plt.grid()
plt.legend()

plt.subplot(312)
plt.plot(timp, semnal_sawtooth)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Tip "Sawtooth"')
plt.grid()
plt.legend()

plt.subplot(313)
plt.plot(timp, suma_semna)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Suma Semnalelor')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


#6

import numpy as np
import matplotlib.pyplot as plt

fs = 50

durata = 1

num_eșantioane = int(fs * durata)

t = np.linspace(0, durata, num_eșantioane)

f1 = fs / 2
f2 = fs / 4
f3 = 0

semnal1 = np.sin(2 * np.pi * f1 * t)
semnal2 = np.sin(2 * np.pi * f2 * t)
semnal3 = np.sin(2 * np.pi * f3 * t)

plt.figure(figsize=(12, 8))

plt.subplot(311)
plt.plot(t, semnal1)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal cu f = fs/2')
plt.grid()
plt.legend()

plt.subplot(312)
plt.plot(t, semnal2)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal cu f = fs/4')
plt.grid()
plt.legend()

plt.subplot(313)
plt.plot(t, semnal3)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal cu f = 0')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()


