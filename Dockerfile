# inspired by https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287

FROM python:3.7-slim

# install poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# copy the code
COPY ./src/ app/
WORKDIR /app
RUN export PYTHONPATH=/app/

# set up dependencies
# FIXME: these will not change as often so they should happen first!
COPY pyproject.toml /app
RUN poetry install --no-dev


ENTRYPOINT ["python3", "/app/main.py"]

