
from libs.data_generator import DataSource

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def get_data(event,context):

    log.info(event)

    data = DataSource.get_data()

    for item in data:
        log.info(f'Processed item {item}')
    
    return len(data)
