from scipy.io import wavfile
from scipy import signal
import rpca
import matplotlib.pyplot as plt
import numpy as np



file="new.wav"
output="out"
rate,data=wavfile.read(file)
print(data.shape)
masking=1
gain=1
fs=1024
nperseg=1024
noverlap=nperseg/4

#computing stft
f,t,data_stft=signal.stft(data)

#plot
plt.figure()
plt.pcolormesh(t, f, np.abs(data_stft), vmin=0, vmax=amp)
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()



#computing RPCA

L,S=rpca.robust_pca(data_stft)

plt.figure()
plt.pcolormesh(t, f, np.abs(L), vmin=0, vmax=amp)
plt.ylim([f[1], f[-1]])
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.yscale('log')
plt.show()

#masking
if masking :
    mask=np.array(double(abs(S)>(gain*abs(L))))
    S_mask=mask*data_stft
    L_mask=data_stft-S_mask
    S=S_mask
    L=L_mask



#computing istft
timeL,wavout_L=signal.istft(L,fs=fs,nperseg=nperseg,noverlap=noverlap)
timeS,wavout_S=signal.istft(S,fs=fs,nperseg=nperseg,noverlap=noverlap)

vocal=output+"_vocal.wav"
music=output+"_music.wav"

wavfile.write(vocal,rate,wavout_S)
wavfile.write(music,rate,wavout_L)





