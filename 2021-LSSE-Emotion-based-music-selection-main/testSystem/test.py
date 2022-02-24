from pandas import read_csv
import requests
import random
import pandas as pd
import sys
from flask import Flask, Response, flash, request, redirect, send_from_directory
import pandas as pd
from time import sleep

MONITORING_SESSIONS = 20
DEVEL_SESSIONS = 5

ING_URL_DEVEL = 'http://127.0.0.1:5004/ingestion/dataset'
ING_URL_EXE = 'http://127.0.0.1:5004/ingestion/session'

def test(mode):
    if mode == 1:
        print("RUNNING DEVELOPMENT TEST")
        ### DEVELOPMENT ###
        for i in range(DEVEL_SESSIONS):
            print("RUNNING DEVELOPMENT TEST - Session: ", i)
            files = {'calendar': open('devel_dataset/emotionDrivenMusicSelection_calendar.csv', 'rb'),
                 'headset': open('devel_dataset/emotionDrivenMusicSelection_headset.csv', 'rb'),
                 'labels': open('devel_dataset/emotionDrivenMusicSelection_labels.csv', 'rb'),
                 'setting': open('devel_dataset/emotionDrivenMusicSelection_setting.csv', 'rb')
                 }
            requests.get('http://127.0.0.1:5009/testend') # start timer
            rr = requests.post(ING_URL_DEVEL, files=files)  # send dataset files
            print(rr.text)
            #sleep(70)

    elif mode == 2:
        print("RUNNING EXECUTION TEST")
        ### EXECUTION ###
        for i in range(MONITORING_SESSIONS):
            print("RUNNING EXECUTION TEST - Session: ", i)
            files = {'calendar': open('monitoring_dataset/calendar.csv', 'rb'),
                 'headset': open('monitoring_dataset/headset.csv', 'rb'),
                 'labels': open('monitoring_dataset/labels.csv', 'rb'),
                 'setting': open('monitoring_dataset/setting.csv', 'rb')
                 }
            if i < 1:
                requests.get('http://127.0.0.1:5009/testend') # start timer
            rr = requests.post(ING_URL_EXE, files=files)  # send dataset files
            print(rr.text)
            #sleep(15)




if __name__ == "__main__":
    mode = int(sys.argv[1])
    test(mode)

