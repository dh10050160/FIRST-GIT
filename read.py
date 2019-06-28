import time
from firebase import firebase
job = firebase.FirebaseApplication('https://noidea-annie0.firebaseio.com/', None)

earn = job.get('/June',None)

for key,value in earn.items():
    print('日期={}\t名子={}\t時數={}'.format(value['日期'],value['名子'],value['時數']))
    time.sleep(1)