FROM python:3.7-slim-stretch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /code

WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
# RUN pip uninstall PyJWT
# RUN pip install PyJWT==1.7.0

COPY . /code/

EXPOSE 8085

# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py collectstatic --no-input
# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8085"]
# CMD [ "gunicorn Core.wsgi:application --bind 0.0.0.0:8000" ]