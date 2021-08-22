FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pdm==1.8.0 &&\
    pdm install
CMD ["pdm", "run", "python", "app.py"]