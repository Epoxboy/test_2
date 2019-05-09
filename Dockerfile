FROM python:2.7-slim
WORKDIR /usr/src/app
ARG COMMIT_HASH
RUN echo ${COMMIT_HASH} > ./commithash && pip install flask-restful
COPY ./app/app.py .
CMD [ "python", "./app.py" ]