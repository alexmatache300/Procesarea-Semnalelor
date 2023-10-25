# 1

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

amplitudine = 2.0
frecventa = 1.0
faza = np.pi / 4

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

plt.subplot(212)
plt.plot(timp, semnal_cosinus, label='Semnal Cosinusoidal')
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Cosinusoidal')
plt.grid()

plt.tight_layout()
plt.show()

# 4

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

plt.subplot(312)
plt.plot(timp, semnal_sawtooth)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal Tip "Sawtooth"')
plt.grid()

plt.subplot(313)
plt.plot(timp, suma_semna)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Suma Semnalelor')
plt.grid()

plt.tight_layout()
plt.show()

# 6

fs = 50

durata = 1

num_esantioane = int(fs * durata)

t = np.linspace(0, durata, num_esantioane)

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

plt.subplot(312)
plt.plot(t, semnal2)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal cu f = fs/4')
plt.grid()

plt.subplot(313)
plt.plot(t, semnal3)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('Semnal cu f = 0')
plt.grid()

plt.tight_layout()
plt.show()


# 3

def play_and_record(signal, fs, filename):
    sd.play(signal, fs)
    sd.wait()
    wavfile.write(filename, fs, signal)


# Semnalul generat la exercițiul 2a
f_a = 400
num_esantioane_a = 1600
T_a = 1 / f_a
T_esantionare_a = T_a / num_esantioane_a
t_a = np.arange(0, num_esantioane_a) * T_esantionare_a
semnal_a = np.sin(2 * np.pi * f_a * t_a)

play_and_record(semnal_a, 44100, "semnal_2a.wav")

fs, semnal_incarcat = wavfile.read("semnal_2a.wav")
print(f"Rata de eșantionare a semnalului încărcat (2a): {fs} Hz")

# Semnalul generat la exercițiul 2b
f_b = 800
durata_b = 3.0
num_esantioane_b = int(f_b * durata_b)
T_b = 1 / f_b
T_esantionare_b = T_b / num_esantioane_b
t_b = np.arange(0, num_esantioane_b) * T_esantionare_b
semnal_b = np.sin(2 * np.pi * f_b * t_b)

play_and_record(semnal_b, 44100, "semnal_2b.wav")

fs, semnal_incarcat_b = wavfile.read("semnal_2b.wav")
print(f"Rata de eșantionare a semnalului încărcat (2b): {fs} Hz")

# Semnalul generat la exercițiul 2c
f_c = 240
durata_c = 3.0
num_esantioane_c = int(durata_c * f_c)
T_c = 1 / f_c
T_esantionare_c = T_c / num_esantioane_c
t_c = np.arange(0, num_esantioane_c) * T_esantionare_c
semnal_c = 2 * (t_c * f_c - np.floor(t_c * f_c + 0.5))

play_and_record(semnal_c, 44100, "semnal_2c.wav")

# Semnalul generat la exercițiul 2d
f_d = 300
durata_d = 3.0
num_esantioane_d = int(durata_d * f_d)
timp_d = np.linspace(0, durata_d, num_esantioane_d)
semnal_d = np.sign(np.sin(2 * np.pi * f_d * timp_d))

# Redare și înregistrare a semnalului 2d
play_and_record(semnal_d, 44100, "semnal_2d.wav")

fs, semnal_incarcat_d = wavfile.read("semnal_2d.wav")
print(f"Rata de eșantionare a semnalului încărcat (2d): {fs} Hz")

fs, semnal_incarcat_c = wavfile.read("semnal_2c.wav")
print(f"Rata de eșantionare a semnalului încărcat (2c): {fs} Hz")

# 2
amplitudine = 1.0
frecventa = 3.0
num_esantioane = 50
faze = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]  # 4 valori diferite pentru fază

t = np.linspace(0, 1, num_esantioane)

semnale = [amplitudine * np.sin(2 * np.pi * frecventa * t + faza) for faza in faze]

snr_valori = [0.1, 1, 10, 100]

z = np.random.normal(0, 1, num_esantioane)

plt.figure(figsize=(10, 6))
for i in range(len(semnale)):
    semnal = semnale[i]
    snr_dorit = snr_valori[i]

    norma_semnal = np.linalg.norm(semnal)
    norma_zgomot = np.linalg.norm(z)
    gamma = np.sqrt((norma_semnal ** 2) / (snr_dorit * (norma_zgomot ** 2)))

    semnal_zgomotizat = semnal + gamma * z

    plt.plot(t, semnal_zgomotizat, label=f'Fază = {faze[i]}, SNR = {snr_dorit}')

plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnale Sinusoidale Zgomotizate ')
plt.grid(True)
plt.show()
