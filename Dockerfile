# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Install pip requirements
RUN apt-get install libmysqlclient-dev
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
