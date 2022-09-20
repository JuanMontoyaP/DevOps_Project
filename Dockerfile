FROM python:3.10.6-alpine

WORKDIR /usr/src/app

COPY ["requirements.txt", "."]

RUN pip install --no-cache-dir -r requirements.txt

COPY ["./app", "."]

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["main.py"]