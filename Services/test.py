#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer

if __name__ == '__main__':
    config = {
        #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
        'host':'identify-us-west-2.acrcloud.com',
        'access_key':'ea6de2ce8a73411249b7f300ade436a3',
        'access_secret':'nB3rKGAR3BH3OW0BBkBsx4dX6ExjuRmMRnur1NGC',
        'timeout':10 # seconds
    }

    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print( re.recognize_by_file(sys.argv[1], 0))

    buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print( re.recognize_by_filebuffer(buf, 0))
