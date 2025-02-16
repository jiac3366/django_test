
#### Quick Start

```bash
docker compose up
```

#### API TEST

pls note that attch the `-H 'Content-Type: application/json'` to generate request 

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

curl -X POST 'http://localhost:8000/signin/' \
-H 'Content-Type: application/json' \
-d '{
    "email": "test@test.com",
    "password": "123"
}'

```

- `/me/`, testing request, pls replace the token with the one responed from `/signin/`

```bash

curl 'http://localhost:8000/me/' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NzU3OTIzLCJpYXQiOjE3Mzk3MTQ3MjMsImp0aSI6Ijg2OTY1NTM1OWQyOTQ0ZjVhYTEzNWE1OGY4ZTYzNDMxIiwidXNlcl9pZCI6OX0.NNplYvCfAMbw5PDP4ZF7zas3NsDEKGuh9hNU-mNM1gw'

```


#### result

![alt text](result.png)