import requests as rq
import logging
import requests.exceptions

# объект логирования и форматирование записей для вывода в консоль
formatting = '[%(asctime)s] [%(levelname)s]: %(message)s'
logging.basicConfig(level=logging.INFO, format=formatting)
logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/',
         'https://instagram.com',
         'https://wikipedia.org',
         'https://yahoo.com',
         'https://yandex.ru',
         'https://whatsapp.com',
         'https://twitter.com',
         'https://amazon.com',
         'https://tiktok.com',
         'https://www.ozon.ru']

# файлы для записи результатов
success_log = 'success_response.log'  # INFO
bad_log = 'bad_responses.log'  # WARNING
blocked_log = 'blocked_response.log'  # ERROR


def write_to_file(file_name, message):
    '''запись в файл лога'''
    with open(file_name, 'a') as file:
        file.write(message + '\n')


for site in sites:
    try:
        response = rq.get(site, timeout=3)

        if response.status_code == 200:
            logging.info(f'{response.status_code}')
            write_to_file(success_log, site)

        elif response.status_code != 200:
            logging.warning(f'{response.status_code}')
            write_to_file(bad_log, site)

    except requests.exceptions.RequestException as e:
        logging.error(f'No Connection')
        write_to_file(blocked_log, str(site) + ':' + str(e))
