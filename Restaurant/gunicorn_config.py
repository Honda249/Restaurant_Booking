# gunicorn_config.py

bind = '0.0.0.0:8000'  # The address and port on which to listen
workers = 3             # The number of worker processes for handling requests
