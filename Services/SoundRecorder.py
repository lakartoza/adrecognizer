import numpy as np
import sounddevice as sd
import pydub

class SoundRecorder:
	"""docstring for SoundRecorder"""
	def __init__(self):
		super(SoundRecorder, self).__init__()
		self.samplerate = 44100
		self.channels = 2
		


	def recordOneBuffer(self, bufferDuration):
		duration =bufferDuration
		sd.default.samplerate = fs = self.samplerate
		sd.default.channels = self.channels

		myrecording = sd.rec(int(duration * fs), blocking=True)
		return myrecording

	def playSound(self, soundBuffer): 
		sd.play(soundBuffer)
		sd.wait()

		return 0


	def readMp3File(self, f, normalized=False):
	    """MP3 to numpy array"""
	    a = pydub.AudioSegment.from_mp3(f)
	    y = np.array(a.get_array_of_samples())
	    if a.channels == 2:
	        y = y.reshape((-1, 2))
	    if normalized:
	        return a.frame_rate, np.float32(y) / 2**15
	    else:
	        return a.frame_rate, y


	def writeMp3(self, fileurl, soundBuffer):
	    """numpy array to MP3"""
	    y = np.int16(soundBuffer * 2 ** 15)
	    song = pydub.AudioSegment(y.tobytes(), frame_rate=self.samplerate, sample_width=2, channels=self.channels)
	    song.export(fileurl, format="mp3", bitrate="320k")
	    return fileurl

