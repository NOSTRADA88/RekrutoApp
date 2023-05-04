FROM python:3.11.3-slim
ENV PYTHONUNBUFFERED 1
LABEL authors="nostrada"

WORKDIR /test

COPY ./requirements.txt /test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt

COPY . /test

CMD ["uvicorn", "test.main:app", "--host", "0.0.0.0", "--port", "80"]