# Python Sample API

## Overview
- Sample API based on [Flask](https://flask.palletsprojects.com/en/2.3.x/)

## Getting started
- Uses [Poetry](https://python-poetry.org/)

### Initial setup
Run (first time only):

```
poetry install
```

This will install all necessary dependencies.

### Running the web server

Enter the web app directory
```
cd python_sample_api
```

Run :
```
FLASK_APP=main.py poetry run flask run
```

If on Windows, run this instead:
```
poetry run flask --app main.py run
```

### Test that things work
From a new terminal run (assumes you have `curl` installed):

```
curl localhost:5000
```
