FROM python:3.10

COPY . /docker-flask
WORKDIR /docker-flask

RUN pip install -r requirements.txt

CMD ["python3", "docker-flask.py"]