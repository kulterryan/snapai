import wavio as wv
import sounddevice as sd

# Sampling frequency
freq = 44100

# Recording duration
duration = 10

def record_voice():  
  # Recording Settings
  recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

  # Start Recording
  print("STARTED: Voice Recorder")
  sd.wait()

  # Save Recording
  wv.write("audio/recording.wav", recording, freq, sampwidth=2)