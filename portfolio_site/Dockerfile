FROM python:3-onbuild
COPY . /usr/src/app
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
