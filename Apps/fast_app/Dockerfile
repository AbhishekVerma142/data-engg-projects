FROM python:3.8.14-bullseye
WORKDIR /app
COPY . .
RUN pip install uvicorn fastapi
CMD uvicorn fast_app.main:app --host 0.0.0.0 --port $PORT
