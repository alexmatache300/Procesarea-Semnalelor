import numpy as np
import matplotlib.pyplot as plt
# Lab1PS
#a + b

t = np.arange(0, 0.03, 0.0005)

x = np.cos(520 * np.pi * t + np.pi/3)
y = np.cos(280 * np.pi * t - np.pi/3)
z = np.cos(120 * np.pi * t + np.pi/3)

plt.figure(figsize=(12, 8))

plt.subplot(311)
plt.plot(t, x)
plt.title('1 a si b Semnal x(t) = cos(520πt + π/3)')
plt.grid()

plt.subplot(312)
plt.plot(t, y)
plt.title('1 a si b Semnal y(t) = cos(280πt − π/3)')
plt.grid()

plt.subplot(313)
plt.plot(t, z)
plt.title('1 a si b Semnal z(t) = cos(120πt + π/3)')
plt.grid()

plt.tight_layout()
plt.show()

#c)
fs = 200

plt.figure(figsize=(12, 8))

plt.subplot(311)
t = np.arange(0, 0.03, 0.0005)
x = np.cos(520 * np.pi * t + np.pi/3)
plt.plot(t, x)
t = np.arange(0, 0.03, 1/fs)
x = np.cos(520 * np.pi * t + np.pi/3)
plt.stem(t, x, markerfmt='ro', linefmt='r-')
plt.title('1c) Semnal eșantionat x[n] (Frecvență de eșantionare = 200 Hz)')
plt.grid()

plt.subplot(312)
t = np.arange(0, 0.03, 0.0005)
y = np.cos(280 * np.pi * t - np.pi/3)
plt.plot(t, y)
t = np.arange(0, 0.03, 1/fs)
y = np.cos(280 * np.pi * t - np.pi/3)
plt.stem(t, y, markerfmt='go', linefmt='g-')
plt.title('Semnal eșantionat y[n] (Frecvență de eșantionare = 200 Hz)')
plt.grid()

plt.subplot(313)
t = np.arange(0, 0.03, 0.0005)
z = np.cos(120 * np.pi * t + np.pi/3)
plt.plot(t, z)
t = np.arange(0, 0.03, 1/fs)
z = np.cos(120 * np.pi * t + np.pi/3)
plt.stem(t, z, markerfmt='bo', linefmt='b-')
plt.title('Semnal eșantionat z[n] (Frecvență de eșantionare = 200 Hz)')
plt.grid()

plt.tight_layout()
plt.show()

#2 a

f = 400

num_eșantioane = 1600

T = 1 / f

T_eșantionare = T / num_eșantioane

t = np.arange(0, num_eșantioane) * T_eșantionare

semnal = np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 4))
plt.plot(t, semnal)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('2a) Semnal sinusoidal de 400 Hz cu 1600 de eșantioane')
plt.grid()
plt.show()



#b
f = 800

durata = 3.0

num_eșantioane = int(f * durata)

T = 1 / f

T_eșantionare = T / num_eșantioane

t = np.arange(0, num_eșantioane) * T_eșantionare

semnal = np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 4))
plt.plot(t, semnal)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('2b) Semnal sinusoidal de 800 Hz cu durata de 3 secunde')
plt.grid(True)
plt.show()

#c

f = 240

durata = 3.0

numar_eșantioane = int(durata * f)

T = 1 / f

T_eșantionare = T / num_eșantioane

t = np.arange(0, num_eșantioane) * T_eșantionare

semnal = 2 * (t * f - np.floor(t * f + 0.5))

plt.figure(figsize=(10, 4))
plt.plot(t, semnal)
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.title('2c) Semnal tip "sawtooth" de 240 Hz')
plt.grid(True)
plt.show()


#d

f = 300

durata = 3.0

numar_eșantioane = int(durata * f)

timp = np.linspace(0, durata, numar_eșantioane)

semnal = np.sign(np.sin(2 * np.pi * f * timp))

plt.plot(timp, semnal)
plt.title('2d) Semnal Square de 300 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()


#e

x = 128
y = 128

semnal = np.random.rand(x, y)

plt.imshow(semnal, cmap='gray')
plt.title('2e) Semnal 2D Random')
plt.show()


#3

#(a) Intervalul de timp între două eșantioane este inversul frecvenței de eșantionare. Frecvența de eșantionare este de 2000 Hz, deci intervalul de timp este:

#Interval de timp = 1 / Frecvența de eșantionare = 1 / 2000 = 0.0005 secunde (0.5 milisecunde).

#b

frecventa_eșantionare = 2000

numar_biti_pe_eșantion = 4

durata_achizitie_ore = 1

ore_in_secunde = 3600

numar_total_bytes = (frecventa_eșantionare * durata_achizitie_ore * ore_in_secunde * numar_biti_pe_eșantion)/8

print(f'Numărul total de bytes necesari: {numar_total_bytes} bytes')

