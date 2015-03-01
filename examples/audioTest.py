__author__ = 'lli5ba'

import pyaudio
import wave

#define stream chunk
chunk = 1024

#open a wav format music
f = wave.open('\Users\Student\PycharmProjects\myo-python\sounds\prac_tom.wav')
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#paly stream
while data != '':
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()