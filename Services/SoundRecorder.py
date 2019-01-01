
import sounddevice as sd

class SoundRecorder:
	"""docstring for SoundRecorder"""
	def __init__(self):
		super(SoundRecorder, self).__init__()
		self.bufferDuration = 2.0 # seconds
		self.samplerate = 44100
		self.channels = 2
		


	def recordOneBuffer(self):
		duration =self.bufferDuration
		sd.default.samplerate = fs = self.samplerate
		sd.default.channels = self.channels

		myrecording = sd.rec(int(duration * fs), blocking=True)
		return myrecording


