FROM python:3.8-slim-buster


RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

CMD ["python3","app.py"]