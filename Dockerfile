FROM python:3.9-buster

LABEL MAINTAINER="has.to.be emobility "

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD ./requirements.txt ./requirements.txt

WORKDIR .

RUN pip install --upgrade pip
RUN pip3 install -r  requirements.txt

COPY ./ /.

EXPOSE 8000
CMD ["gunicorn", "python3 manage.py --noinput", "--chdir", "--bind", "0.0.0.0:8000", "csms.csms.wsgi:application"]
