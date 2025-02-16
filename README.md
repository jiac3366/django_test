
#### Quick Start

```bash
uv venv
uv sync
uv run python manage.py runserver
```

#### API TEST

- `/signup/`, testing request:

```bash
curl -X POST 'http://localhost:8000/signup/' \
-H 'Content-Type: application/json' \
-d '{
    "email": "test@test.com",
    "password": "123"
}'
```

- `/signin/`, testing request:

```bash

curl -X POST 'http://localhost:8000/token/signin/' \
-H 'Content-Type: application/json' \
-d '{
    "email": "test@test.com",
    "password": "123"
}'

```

- `/me/`, testing request, pls replace the token with the one responed from `/signin/`

```bash

curl 'http://localhost:8000/api/me/' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NzEzMzc2LCJpYXQiOjE3Mzk3MTMwNzYsImp0aSI6IjVmMTU1ZTFlMzIwYzQ3MjI4NDcwMThiZDhkYTcyMmU2IiwidXNlcl9pZCI6Nn0.FhCfOCfu5qu-htPQej4L88cSRJANmvZdaKw2LJxHWxg'

```
