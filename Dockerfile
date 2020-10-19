FROM python:3.8-slim

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./infrafinder.py /opt/infrafinder.py
COPY ./secrets.py /opt/secrets.py
WORKDIR /opt
ENTRYPOINT ["python", "-u", "infrafinder.py"]
