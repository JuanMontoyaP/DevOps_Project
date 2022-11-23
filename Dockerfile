FROM python:3.10.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env ./app ./

ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["main.py"]