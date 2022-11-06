FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY ./producer.py /app/

COPY ./requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --user

EXPOSE 8000
EXPOSE 31000

CMD [ "python3", "producer.py" ]