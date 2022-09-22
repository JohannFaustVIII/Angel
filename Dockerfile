FROM python:latest

WORKDIR /app

RUN python -m pip install pip

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /random .