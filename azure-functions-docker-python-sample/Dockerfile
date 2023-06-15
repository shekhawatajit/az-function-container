FROM mcr.microsoft.com/azure-functions/python:3.0-python3.6

ENV host:logger:consoleLoggingMode=always

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && pip install -r requirements.txt
