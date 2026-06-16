FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# Apply migrations, then serve. The stack deploys the database component first,
# so the DB is reachable by the time this runs.
CMD ["sh", "-c", "python manage.py migrate && gunicorn -b 0.0.0.0:8000 mysite.wsgi"]
