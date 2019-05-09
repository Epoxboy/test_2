FROM python:2
WORKDIR /usr/src/app
RUN pip install flask-restful
COPY ./app/app.py .
CMD [ "python", "./app.py" ]