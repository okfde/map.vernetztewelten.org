FROM python:3.7.2
RUN apt-get update && apt-get install -y libgdal-dev
COPY requirements.txt /code/
WORKDIR /code
RUN pip install wheel && pip install -r requirements.txt

ENV PYTHONPATH /code
COPY manage.py manage.py
COPY vernetztemap vernetztemap

RUN mkdir static && python manage.py collectstatic --noinput
RUN python manage.py compress -f

COPY static /code/static

CMD python manage.py runserver 0.0.0.0:8000
