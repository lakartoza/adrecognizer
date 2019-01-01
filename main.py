


from Services import SoundRecorder


def main(): 

	recorder = SoundRecorder.SoundRecorder()

	myrecording = recorder.recordOneBuffer()

	print(myrecording)

	return 0


if __name__ == '__main__':
	main()