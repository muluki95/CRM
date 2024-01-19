FROM python:3.8-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /django

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Update pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
