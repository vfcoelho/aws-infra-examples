import os
from dateutil import parser
from dateutil.tz.tz import tzutc
from datetime import datetime
import uuid
import random

class DataSource():

    @classmethod
    def get_data(cls):
        limit_date = parser.parse(os.environ.get('dataSourceDateLimit'))
        now = datetime.utcnow()
        now.replace(tzinfo=tzutc())
        result = []
        if limit_date > now:
            items = round(random.random()/2,1)*10
            for item in range(int(items)):
                result.append(uuid.uuid4())
        return result
