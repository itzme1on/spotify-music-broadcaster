print('by Aradionov366')
print('====Telegram====')
print('api id и api hash получать на my.telegram.org')
f = open('bd.py', 'w')
api_id = input('Введите api id: ') #my.telegram.org
api_hash = input('Введите api hash: ') #my.telegram.org
f.write(f'api_id = {api_id}\napi_hash = "{api_hash}"\n')
print('====Spotify====')
print('client id и client secret получать на https://developer.spotify.com/dashboard/')
client_id = input('Введите client id: ')
client_secret = input('Введите client secret: ')
redirect_uri = "http://localhost:8888/callback" #Не трогать (!)
spotiusername = input('Введите юзернейм в spotify: ')
f.write(f'client_id = "{client_id}"\nclient_secret = "{client_secret}"\nspotiusername = "{spotiusername}"\n')
print('====Дополнительные функции====')
status = input('Введите статус, который будет поставлен при условии, что spotify не работает: ')
f.write(f'status = "{status}"')
f.close()
print(f'хорошо, скрипт настроен, авторизируйте spotify через эту ссылку:\nhttps://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope=user-read-playback-state-user-libary-read&redirect_uri=http://localhost:8888/callback')
