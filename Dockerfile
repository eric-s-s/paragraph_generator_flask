FROM python:3.7

ADD . /code/
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["uwsgi", "--ini", "uwsgi_config.ini"]
#CMD ["gunicorn", "--config", "gunicorn_config.py", "paragraph_generator.flask_app:create_app"]
#CMD ["flask","run","--host=0.0.0.0","--port=8080"]
