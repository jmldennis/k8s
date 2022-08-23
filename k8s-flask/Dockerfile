FROM python:3.10

COPY . /k8sflask
WORKDIR /k8sflask

RUN pip install -r requirements.txt

CMD ["python3", "k8sflask.py"]