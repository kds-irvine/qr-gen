FROM python:latest

COPY app .

RUN pip install -r requirements.txt

expose 9000

CMD [ "python", "-u", "run.py" ]

