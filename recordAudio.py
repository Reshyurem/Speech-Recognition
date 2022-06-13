from pickle import FRAME
import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 72000

audioObj = pyaudio.PyAudio()

stream = audioObj.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Recording has started")

seconds = 10
frames = []

# Calculate the number of buffers to read the length of the audio file
# Then record each buffer and add it to the frames list
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()

print("Recording has Ended")

audioObj.terminate()

newFile = wave.open("Giorgio.wav", "wb")
newFile.setnchannels(CHANNELS)
newFile.setsampwidth(audioObj.get_sample_size(FORMAT))
newFile.setframerate(RATE)

newFile.writeframes(b"".join(frames))
newFile.close()