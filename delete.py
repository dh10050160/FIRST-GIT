def checkid():
    id=''
    if datas != None:
        for key in datas:
            if day == datas[key]['日期']:
                id = key
                break
    return id

from firebase import firebase
job = firebase.FirebaseApplication('https://noidea-annie0.firebaseio.com/', None)

while True:
    datas = job.get('/June',None)
    day = input('請輸入日期')
    if day == '' :break
    id = checkid()
    if id != '' :
        print('確定刪除{}'.format(datas[id]['名子']))
        yn=input('y/n')
        if yn == 'y':
            job.delete('/June/'+id,None)
            print('已刪')
    else:
        print('{}沒有'.format(day))