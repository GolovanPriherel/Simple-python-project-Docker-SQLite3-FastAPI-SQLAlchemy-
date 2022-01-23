FROM python:3.9

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src /src
COPY main.py main.py

CMD [ "python3", "main.py" ]