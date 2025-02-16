
#### Quick Start

```bash
uv venv
uv sync
uv run python manage.py runserver
```

#### API 

- `/signup/`, testing request:

```bash
curl --request POST \
  --url http://localhost:8000/signup/ \
  --header 'content-type: application/json' \
  --data '{
	"email": "test@test.com",
	"password": "123"
}'
```

- `/signin/`, testing request:

```bash
curl --request POST \
  --url http://localhost:8000/signup/ \
  --header 'content-type: application/json' \
  --data '{
	"email": "test@test.com",
	"password": "123"
}'

```

- `/me/`, testing request:

