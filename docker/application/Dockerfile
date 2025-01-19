FROM python:3.12-slim

WORKDIR /app
COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app with arguments
ENTRYPOINT ["python", "main.py"]