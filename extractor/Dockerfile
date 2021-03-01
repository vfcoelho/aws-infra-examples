FROM amazonlinux

ADD vendored /vendored
ADD libs /libs
ADD workers /workers

RUN yum -y install python3


CMD ["python3", "workers/extractor_worker.py"]