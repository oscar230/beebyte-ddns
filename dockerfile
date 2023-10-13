FROM python:3-slim

WORKDIR /usr/src/app

COPY *.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./program.py"]
