FROM python:3.10.8-slim-buster

COPY ./precium .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["--version"]
