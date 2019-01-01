
import unittest
import sounddevice as sd
import numpy as np


class TestSoundRecorder(unittest.TestCase):


    def test_recorderCreatesRecording(self):
        duration = 0.5  # seconds
        sd.default.samplerate = fs = 44100
        sd.default.channels = 2

        myrecording = sd.rec(int(duration * fs))
        zeros = np.zeros((int(duration*fs), 2))

        print(zeros.tolist() == myrecording.tolist())

        print(myrecording.shape)
        print(zeros.shape)

        self.assertNotEqual(myrecording.tolist()[10:30], zeros.tolist()[10:30])



    # def test_recorderRunsInBackground(self):






if __name__ == '__main__':
    unittest.main()
