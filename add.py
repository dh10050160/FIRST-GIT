from firebase import firebase

while True:
    date = input('日期')
    name = input('名子')
    time = input('時數(小時)')
    day = [{'日期':date,'名子':name,'時數':time+'小時'}]

    job = firebase.FirebaseApplication('https://noidea-annie0.firebaseio.com/', None)


    for day in day:
        job.post('/June',day)
        print('finish'.format(day))