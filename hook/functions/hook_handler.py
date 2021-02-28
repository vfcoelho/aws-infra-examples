import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

import json

def receive_data(event,context):
    log.info('Event Received!')
    log.info(event)

    message = event['Records'][0]
    call = json.loads(message.get('body','{}'))

    log.info(call)

    type_node_raise = {
        'Hook': lambda call: call.get('body',{}).get('raise'),
        'Notification': lambda call: json.loads(call.get('Message','{}')).get('raise')
    }

    if type_node_raise[call.get('Type')](call):
        raise Exception('Error raised manually')