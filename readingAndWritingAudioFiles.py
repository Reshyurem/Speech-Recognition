import wave

file = wave.open("Greetings.wav", "rb")

print("Number of channels: ", file.getnchannels())
print("Sample width: ", file.getsampwidth())
print("Frame rate: ", file.getframerate())
print("Number of frames: ", file.getnframes())
print("Parameters: ", file.getparams())

frames = file.readframes(-1)
print("Type:", type(frames))
print("Type of Individual Frames:", type(frames[0]))
print("Length:", len(frames) / file.getnchannels())
print("First 10 bytes:", frames[:10])

file.close()

newFile = wave.open("Greetings_Mono.wav", "wb")

newFile.setnchannels(1)
newFile.setsampwidth(2)
newFile.setframerate(72000)

newFile.writeframes(frames)

newFile.close()