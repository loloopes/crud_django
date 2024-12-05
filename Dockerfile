FROM python:3.13.0-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Download wait-for-it.sh
RUN curl -o /app/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /app/wait-for-it.sh

RUN chmod +x /app/django.sh

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]
