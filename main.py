import logging
import os
import time

import requests
import telegram

from dotenv import load_dotenv

logger = logging.getLogger(__file__)


def check_lessons(devman_token, poll_timeout):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': f'Token {devman_token}'}
    payload = {'timestamp': poll_timeout}
    response = requests.get(url=url, headers=headers, params=payload, timeout=120)
    response.raise_for_status()
    return response.json()


def send_lesson_tg(bot, chat_id, lessons):
    text = ''
    for lesson in lessons:
        text = (
            f'У вас проверили работу ["{lesson["lesson_title"]}"]'
            f'({lesson["lesson_url"]})\n'
        )
        if lesson['is_negative']:
            text += 'К сожалению в работе нашлись ошибки.'
        else:
            text += 'Преподавателю всё понравилось, можно приступать к следующему уроку!'
        bot.send_message(chat_id=chat_id, text=text, parse_mode='markdown')


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    load_dotenv()
    devman_token = os.environ.get('DEVMAN_TOKEN')
    tg_token = os.environ.get('TG_TOKEN')
    tg_chat_id = os.environ.get('TG_CHAT_ID')
    bot = telegram.Bot(token=tg_token)
    poll_timeout = None
    while True:
        try:
            change_lessons = check_lessons(devman_token, poll_timeout)
            if change_lessons['status'] == 'found':
                poll_timeout = change_lessons['last_attempt_timestamp']
                send_lesson_tg(bot, tg_chat_id, change_lessons["new_attempts"])
                logger.info(f'Found {change_lessons["new_attempts"]}')
                continue
            poll_timeout = change_lessons['timestamp_to_request']
        except requests.exceptions.Timeout:
            logger.info(f'Request timeout')
            continue
        except requests.exceptions.ConnectionError:
            logger.info(f'Connection error')
            time.sleep(10)
            continue


if __name__ == '__main__':
    main()
