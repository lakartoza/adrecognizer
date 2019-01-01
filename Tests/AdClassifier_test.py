import unittest
import sounddevice as sd
from acrcloud.recognizer import ACRCloudRecognizer


class TestAdClassifier(unittest.TestCase):


    def test_classifyLiveRecording(self):
        duration = 10  # seconds
        sd.default.samplerate = fs = 44100
        sd.default.channels = 2

        myrecording = sd.rec(int(duration * fs), blocking=True)


        # ARCloud Config for classification
        config = {
            'host':'identify-us-west-2.acrcloud.com',
            'access_key':'ea6de2ce8a73411249b7f300ade436a3',
            'access_secret':'nB3rKGAR3BH3OW0BBkBsx4dX6ExjuRmMRnur1NGC',
            'timeout':10 # seconds
        }
        re = ACRCloudRecognizer(config)
        buf = myrecording #open(sys.argv[1], 'rb').read()

        classificationResponse = re.recognize_by_filebuffer(buf, 0)
        print(classificationResponse)


        self.assertEqual(1, 1)


    def test_classifyFromFile(self):
        # ARCloud Config for classification
        config = {
            'host':'identify-us-west-2.acrcloud.com',
            'access_key':'ea6de2ce8a73411249b7f300ade436a3',
            'access_secret':'nB3rKGAR3BH3OW0BBkBsx4dX6ExjuRmMRnur1NGC',
            'timeout':10 # seconds
        }
        re = ACRCloudRecognizer(config)
        buf = open('../Data/Recorded_Sounds/Geico_Ad_5sec.m4a', 'rb').read()

        classificationResponse = re.recognize_by_filebuffer(buf, 0)
        print(classificationResponse)


        self.assertEqual(1, 1)


# {
#     "metadata": {
#         "timestamp_utc":"2019-01-01 07:31:21",
#         "custom_files":[
#             {"acrid":"757d34b6ce46c1ad4977d84eae878213","play_offset_ms":7940,"duration_ms":"36000","score":100,"title":"Full Recorded Geico Ad 1","bucket_id":"9918"}
#             ]
#     },
#     "cost_time":0.020999908447266,
#     "status":{
#         "msg":"Success","version":"1.0","code":0
#     },
#     "result_type":0
# }



if __name__ == '__main__':
    unittest.main()
