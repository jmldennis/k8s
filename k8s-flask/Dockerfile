FROM python:3.10

COPY . /k8s-flask
WORKDIR /k8s-flask

RUN pip install -r requirements.txt

CMD ["python3", "k8s-flask.py"]