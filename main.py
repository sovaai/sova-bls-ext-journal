import logging
from external_modules.journal.models import (JournalModel)
import datetime


async def store_info(message):
    """
        Сохранение данных в Базе данных
    :param message:
    :return:
    """
    journal = JournalModel()
    journal.chat = message['technical_info']['session_id']
    journal.inf = message['technical_info']['inf_id']
    journal.req_ts = message['technical_info']['req_ts']
    if message['type'] == 'request':
        journal.request = message['text']
        journal.is_event = False
    elif message['type'] == 'event':
        journal.request = message['euid']
        journal.is_event = True

    journal.resp_ts = datetime.datetime.now()
    if message['technical_info'].get('not_send_engine'):
        logging.debug(f'journal store {message}')
        journal.resp_cntx = message['technical_info']['technical_context']['last_response']['cntx']
        journal.response = message['technical_info']['technical_context']['last_response']['text']
    else:
        journal.resp_cntx = message['technical_info']['resp_cntx']
        journal.response = message['technical_info']['response']

    journal.req_cntx = message['context']
    await journal.save()


async def main(message):
    logging.debug(f"Обработка сообщения в журнале {message}")
    if message['type'] in ['request', 'event']:
        await store_info(message)
    logging.debug(f"Завершение oбработки сообщения в журнале {message}")
    return message