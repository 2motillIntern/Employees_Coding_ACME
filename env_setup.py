import hashlib
import string
import random


def add_to_env(length):
    with open('.env', 'w+') as file:
        database_url = 'postfresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='Mia$wet16',url='127.0.0.1:5432',db='employee_api_db')
        data = file.read()
        file.seek(0)
        all_letters = string.ascii_lowercase
        letter_connect = ''.join(random.choice(all_letters) for i in range(length))
        key = hashlib.sha224(letter_connect[2::].encode('utf-8'))
        file.write(f'SECRET_KEY={key.hexdigest()}\nDATABASE_URL={database_url}'.replace('\n','\n'))
        file.truncate()

add_to_env(20)