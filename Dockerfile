FROM python:3.8

WORKDIR /MKAD_distance_task

ADD . /MKAD_distance_task

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
