from email import message
from unittest import result
from fastapi.background import P
import requests
import time
from pprint import pprint

TELEGRAM_URL_API = 'https://api.telegram.org/bot'
DOG_URL_API = 'https://random.dog/woof.json'
BOT_TOKEN = '7800792317:AAHF1g9tnCXnhssy637Hworc-2Q6stLhdm4'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2


counter = 0
while counter < 100:
    print(f'attempt = {counter}')
    updates = requests.get(f'{TELEGRAM_URL_API}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['ok']:
        for message in updates['result']:
            offset = message['update_id']
            chat_id = message['message']['chat']['id']
            cat_response = requests.get(DOG_URL_API)
            if cat_response.status_code == 200:
                cat_url = cat_response.json()['url']
                requests.get(f'{TELEGRAM_URL_API}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_url}')
            else:
                requests.get(f'{TELEGRAM_URL_API}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1