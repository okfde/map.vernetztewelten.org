# Culture Map . Eureka

## Local project setup

Start a local PostgreSQL Server with PostGIS installed.

Setup virtualenv and install dependencies:

```
python3 -m venv umap-env
source umap-env/bin/activate
pip install -r requirements.txt
```

Copy `env.example` to `.env` and adjust values.

```
# Load configuration as environment variables
source .env
python manage.py migrate
python manage.py runserver
```

## Local project setup with Docker

```
docker-compose -f docker-compose.dev.yml up
```

## Deployment with Docker

Copy `env.example` to `.env` and adjust values.

```
docker-compose up --build
```

The server will listen by default on port 8000.


## Admin interface

There's an admin interface at `/admin/`. You can create admin users like this:

```
python manage.py createsuperuser
```
