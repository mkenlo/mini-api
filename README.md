# Dependencies

- python 3

# How to run

1. install requirements:
   `pip install -r requirements.txt`
2. run app
   `flask --debug run`
Production environment : `gunicorn --workers 4 --bind 0.0.0.0 app:app`
# Tests

`pytest`
