import wave

__authors__ = 'lli5ba, pmattox2'

# Python API for Myo by Rosenstein


import myo
import pyaudio
from myo.lowlevel import pose_t, stream_emg
from myo.six import print_
import random

myo.init()

SHOW_OUTPUT_CHANCE = 0.5
r"""
There can be a lot of output from certain data like acceleration and orientation.
This parameter controls the percent of times that data is shown.
"""

class Listener(myo.DeviceListener):
    # return False from any method to stop the Hub

    def on_connect(self, myo, timestamp):
        print_("Connected to Myo")
        myo.vibrate('short')
        myo.request_rssi()

    # def on_rssi(self, myo, timestamp, rssi):
    #     print_("RSSI:", rssi)

    def on_event(self, event):
        r""" Called before any of the event callbacks. """

    def on_event_finished(self, event):
        r""" Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub. """

    def on_pair(self, myo, timestamp):
        print_('Paired')
        print_("If you don't see any responses to your movements, try re-running the program or making sure the Myo works with Myo Connect (from Thalmic Labs).")


    # def on_disconnect(self, myo, timestamp):
    #     print_('on_disconnect')

    def on_pose(self, myo, timestamp, pose):
        #print_('on_pose', pose)
        if pose == pose_t.double_tap:
            print_("Double tapped")
        elif pose == pose_t.fingers_spread:
            hi_hat()
            print_("Fingers Spread - hi_hat")

        elif pose == pose_t.wave_in:
            tom_tom()
            print_("Wave in - tom-tom")
        elif pose == pose_t.wave_out:
            cymbal()
            print_("Wave out-cymbal")
        elif pose == pose_t.fist:
            snare()
            print_("Fist-snare")

    # def on_orientation_data(self, myo, timestamp, orientation):
    #     #show_output('orientation', orientation)
    #
    # def on_accelerometer_data(self, myo, timestamp, acceleration):
    #     #show_output('acceleration', acceleration)
    #
    # def on_gyroscope_data(self, myo, timestamp, gyroscope):
    #     #show_output('gyroscope', gyroscope)
    #
    # def on_unlock(self, myo, timestamp):
    #     #print_('unlocked')
    #
    # def on_lock(self, myo, timestamp):
    #     print_('locked')
    #
    # def on_sync(self, myo, timestamp, arm, x_direction):
    #     print_('synced', arm, x_direction)
    #
    # def on_unsync(self, myo, timestamp):
    #     print_('unsynced')
    #
    # def on_emg(self, myo, timestamp, emg):
    #     #show_output('emg', emg)

def show_output(message, data):
    if random.random() < SHOW_OUTPUT_CHANCE:
        print_(message + ':' + str(data))

def hi_hat():
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open('\Users\Student\PycharmProjects\myo-python\sounds\prac_hat.wav')
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
def tom_tom():
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
def snare():
        #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open('\Users\Student\PycharmProjects\myo-python\sounds\prac_snare_2.wav')
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
def cymbal():
        #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open('\Users\Student\PycharmProjects\myo-python\sounds\prac_ride_bell_loud.wav')
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
def main():

    hub = myo.Hub()
    hub.set_locking_policy(myo.locking_policy.none)
    hub.run(1000, Listener())


    # Listen to keyboard interrupts and stop the
    # hub in that case.
    try:
        while hub.running:
            myo.time.sleep(0.2)
    except KeyboardInterrupt:
        print_("Quitting ...")
        hub.stop(True)

if __name__ == '__main__':
    main()

