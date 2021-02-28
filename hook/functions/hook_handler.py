import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

import json

def receive_data(event,context):
    log.info('Event Received!')

    message = event['Records'][0]
    call = json.loads(message.get('body','{}'))

    log.info(call)

    if call.get('body',{}).get('raise'):
        raise Exception('Error raised manually')