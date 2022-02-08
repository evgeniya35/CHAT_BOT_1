import requests
import logging
import os

from pprint import pprint
from dotenv import load_dotenv


logger = logging.getLogger('logger_main')

def get_list_check(devman_token):
    url = 'https://dvmn.org/api/user_reviews/'
    headers = {'Authorization': f'Token {devman_token}'}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    list_check = response.json()
    return list_check


def get_change_check(devman_token):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': f'Token {devman_token}'}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    pprint(response.json())


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    load_dotenv()
    devman_token = os.environ.get('DEVMAN_TOKEN')
    pprint(get_change_check(devman_token))
    # logger.info(f'Posted message {response["response"]["post_id"]}')


if __name__ == '__main__':
    main()