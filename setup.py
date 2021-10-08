used = 0
print('by Aradionov366')
print('====Telegram====')
print('api id и api hash получать на my.telegram.org')
f = open('bd.py', 'w')
f.write(f'used = {used}\n')
api_id = input('Введите api id: ') #my.telegram.org
api_hash = input('Введите api hash: ') #my.telegram.org
f.write(f'api_id = {api_id}\napi_hash = {api_hash}\n')
print('====Spotify====')
print('client id и client secret получать на https://developer.spotify.com/dashboard/applications')
client_id = input('Введите client id: ')
client_secret = input('Введите client secret: ')
redirect_uri = "http://localhost:8888/callback" #Не трогать (!)
spotiusername = input('Введите юзернейм в spotify: ')
f.write(f'client_id = {client_id}\nclient_secret = {client_secret}\nspotiusername = {spotiusername}\n')
print('====Дополнительные функции====')
status = input('Введите статус, который будет поставлен при условии, что spotify не работает: ')
while True:
    try:
        host = int(input('Хотите ли вы ставить скрипт на хост? Из-за нестабильности библиотеки для работы spotify, скрипт может вылетать, чтоб сделать скрипт незавершаемым, напишите 1, если нет - 0: ')
        if host == 1:
            host1 = input('Хорошо, теперь напишите команду, которая нужна для того, чтоб открыть python-файл, пример - python3: ')
                break
        else: 
                break
    except:
        print('Разве это похоже на число?')
f.write(f'host = {host}\nhost1 = {host1}\n')
used = 1
f.write(f'used = {used}\n')
f.close()
print(f'хорошо, скрипт настроен, авторизируйте spotify через эту ссылку:\nhttps://accounts.spotify.com/authorize?response_type=code&client_id={bd.client_id}&scope=user-read-playback-state-user-library-read&redirect_uri=http://localhost:8888')