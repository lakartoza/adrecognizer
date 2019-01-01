


from Services import SoundRecorder
from Services import AdClassifier

def main(): 
	# set up objects #
	classifier = AdClassifier.AdClassifier()
	recorder = SoundRecorder.SoundRecorder()

	# show recording #
	myrecording = recorder.recordOneBuffer(4.0)

	# output to mp3 # 
	# recorder.playSound(myrecording)
	fileUrl = recorder.writeMp3('Data/Recorded_Sounds/random1.mp3', myrecording)
	# print(myrecording)
	# myrecording = open("Data/Recorded_Sounds/Geico_Ad_5sec.m4a", 'rb').read()

	#send to classification
	# classification = classifier.classifyFromBuffer(myrecording)
	classification = classifier.classifyFromFile(fileUrl)

	if classification=='Success':
		print("This is an ad!")
	if classification=='No result':
		print("This is not an ad I recognize")

	return 0


if __name__ == '__main__':
	main()