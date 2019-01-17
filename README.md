# A flask for serving paragraph_generator

This is a micro-service for serving <https://github.com/eric-s-s/paragraph_generator>

All queries to and replies from are in json format. It also
sends a serialized python object which it expects sent back
for parsing


from parent directory
```bash
$ pip install -r requirements.txt
```
```bash
$ export FLASK_APP=flaskapp/myapp.py
$ flask run
```

open your web-browser to `localhost:5000`

