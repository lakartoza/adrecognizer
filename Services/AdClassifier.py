from acrcloud.recognizer import ACRCloudRecognizer
import json


class AdClassifier:
    """docstring for AdClassifier"""
    def __init__(self):
        super(AdClassifier, self).__init__()
        self.host = 'identify-us-west-2.acrcloud.com'
        self.access_key = 'ea6de2ce8a73411249b7f300ade436a3'
        self.access_secret = 'nB3rKGAR3BH3OW0BBkBsx4dX6ExjuRmMRnur1NGC'
        self.timeout = 15 # seconds
        

    def classifyFromBuffer(self, recordedSound):
        # ARCloud Config for classification
        config = {
            'host':self.host,
            'access_key': self.access_key,
            'access_secret': self.access_secret,
            'timeout': self.timeout
        }
        re = ACRCloudRecognizer(config)
        
        classificationResponse = re.recognize_by_filebuffer(recordedSound, 0)
        classificationResponse = json.loads(classificationResponse)

        return(classificationResponse['status']['msg'])
