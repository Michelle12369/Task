FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install build-essential -y
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py


WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r pip-requirements.txt
# uWSGI LTS
RUN pip3 install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
# CMD ["uwsgi", "wsgi.ini"]