FROM python:3.9-slim-buster

WORKDIR /python-docker-sample

COPY ./requirements.txt /python-docker-sample

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

USER 1000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]