FROM python:3

COPY ./precium .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["--version"]
