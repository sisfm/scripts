FROM python:3

WORKDIR /usr/src/app

COPY *.py ./

RUN python -m unittest -v

CMD [ "python", "./basket.py" ]
