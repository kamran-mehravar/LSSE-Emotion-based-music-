from pandas import read_csv
import requests
import random

### FOR TESTING ONLY ###

MON_URL = 'http://127.0.0.1:5001/human/label'
EXE_URL = 'http://127.0.0.1:5000/execution/session'

## INGESTION
data1 = read_csv('test_data/hotspotUrbanMobility-1.csv')
data2 = read_csv('test_data/hotspotUrbanMobility-2.csv')
data = data1.append(data2, ignore_index=True)
data = data.drop('h24', axis=1)
data = data.loc[data['Anomalous'] < 1]
data.to_csv('test_data/preprocessedDataset.csv', index=False)
data = read_csv('test_data/preprocessedDataset.csv')

monitoring_size = 50
not_in_monitoring = 150

# send 1000 sessions to execution system
# 50 sessions are for monitoring - labels are sent to monitoring
# 150 sessions are executed but not accounted for monitoring
for x in range(1000):

    if monitoring_size > 0:
        # get a random session from database
        random_session = random.randint(0, 200)

        r_session = data.iloc[random_session:random_session+1, 4:len(data.columns)]
        session = r_session.to_json()

        rr = requests.post(EXE_URL, json=session)  # send session to execution system
        #print(rr.text)


        # get human label
        hl = data.iloc[random_session:random_session+1, 1]

        human_label = {'label': hl.tolist()}
        r = requests.post(MON_URL, json=human_label)  # send label to monitoring system

        monitoring_size -= 1
    else:
        # get a random session from database
        random_session = random.randint(0, 200)

        r_session = data.iloc[random_session:random_session + 1, 4:len(data.columns)]
        session = r_session.to_json()

        rr = requests.post(EXE_URL, json=session)  # send session to execution system
        #print(rr.text)
        not_in_monitoring -= 1
        if not_in_monitoring == 0:
            not_in_monitoring = 150
            monitoring_size = 50
