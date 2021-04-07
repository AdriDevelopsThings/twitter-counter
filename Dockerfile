FROM python:3.8
WORKDIR /app
ENV PYTHONPATH=/app

RUN python -m pip install --no-cache-dir --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./resources ./resources
COPY ./__main__.py ./__main__.py

CMD ["python", "__main__.py"]