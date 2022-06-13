import wave
import matplotlib.pyplot as plt
import numpy as np

file = wave.open("Greetings_Mono.wav", "rb")

# Get audio data
sampleFreq = file.getframerate()
noOfSamples = file.getnframes()
signalWave = file.readframes(-1)

file.close()

# Length of the audio clip is the number of frames / frames per second
audioLength = noOfSamples / sampleFreq

print(audioLength)

# Convert the audio data to a numpy array
signalArray = np.frombuffer(signalWave, dtype=np.int16)

# Create a linear space to represent the x axis of the plot by representing each frame
times = np.linspace(0, audioLength, num=noOfSamples)

# Plot the audio data
plt.figure(figsize=(10, 5))
plt.plot(times, signalArray)
plt.title("Greetings Audio File")
plt.xlabel("Frame/Time")
plt.ylabel("Signal Amplitude")
plt.xlim(0, audioLength)
plt.show()