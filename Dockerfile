FROM arm32v7/python:3.7.10-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "api:app"]