FROM python:3.9-slim

WORKDIR /app

COPY /requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "manage.py", "runserver", "0:8000"]
