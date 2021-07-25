FROM python:3.8-slim

WORKDIR /

COPY poetry_requirements.txt requirements.txt
RUN pip install poetry

COPY ./src/ src/

RUN export PYTHONPATH=src/

CMD ["python", "src/main.py"]

