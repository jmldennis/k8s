FROM python:3.10

COPY . /k8sFlask
WORKDIR /k8sFlask

RUN pip install -r requirements.txt

CMD ["python3", "k8sFlask.py"]