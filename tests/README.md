# Tests

> main tests are in the `api.tests.py`.
> these are just some debug and unstandard tests.

## server-app

### curl

- add user

```shell
curl -X POST -H 'Content-Type: application/json' -d '{"username": "alialavi", "password": "aA1234%^"}' -i http://127.0.0.1:8000/auth/users/
```

- create refresh and access tokens:

```shell
curl -X POST -H 'Content-Type: application/json'  -d '{"username": "alialavi", "password": "aA1234%^"}'  http://127.0.0.1:8000/auth/jwt/create
```

- get devices

```shell
curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -i http://127.0.0.1:8000/api/v1/devices/
```
