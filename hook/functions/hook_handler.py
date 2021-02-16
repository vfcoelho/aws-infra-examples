import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def receive_data(event,context):
    log.info('Event Received!')
    log.info(event['body'])