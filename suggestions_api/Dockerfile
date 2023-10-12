FROM python:3.10

EXPOSE 8000

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /usr/src
WORKDIR /usr/src

ADD requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

ADD . /usr/src
WORKDIR /usr/src/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
