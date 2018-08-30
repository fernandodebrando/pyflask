FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]