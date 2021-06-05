FROM python:3.9
WORKDIR /usr/app/
RUN pip install flask uwsgi
ENV FLASK_APP=server
EXPOSE 5000
COPY . .
