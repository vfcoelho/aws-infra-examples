import os
import sys
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "."))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

from libs.data_generator import DataSource

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


def main():

    data = True

    while data:
        data = DataSource.get_data()

        for item in data:
            log.info(f'Processed item {item}')


if __name__ == "__main__":
    log.info(f'Job Started in {os.environ["repoName"]} repo, at {os.environ["stage"]} stage for context {os.environ["context"]}.')
    main()
    log.info('Job Finished!')
