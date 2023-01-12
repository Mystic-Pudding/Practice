import librosa 
from matplotlib import pyplot as plt 
import sounddevice as sd 
example_path = librosa.ex('trumpet')

print(example_path)
y,sr = librosa.load(example_path)

x=[i / sr for i in range(len(y))]
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Audio Example Data (trumpet sound)', fontsize=20)
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Signal Amplitude', fontsize=16)
plt.show()