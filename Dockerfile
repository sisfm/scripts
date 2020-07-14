FROM python:3

WORKDIR /usr/src/app

COPY basket.py ./

CMD [ "python", "./basket.py" ]
