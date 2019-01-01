


from Services import SoundRecorder
from Services import AdClassifier

def main(): 

	classifier = AdClassifier.AdClassifier()
	recorder = SoundRecorder.SoundRecorder()

	myrecording = recorder.recordOneBuffer()

	classification = classifier.classifyFromBuffer(myrecording)

	print(classification)

	return 0


if __name__ == '__main__':
	main()