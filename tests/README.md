# Tests

> main tests are in the `api.tests.py`.
> these are just some debug and unstandard tests.

## server-app

### curl

- get token

```shell
curl -X POST -H 'Content-Type: application/json' -d '{"username": "abbas", "password": "1"}' -i http://127.0.0.1:8000/api/token/
```

- get devices

```shell
curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -i http://127.0.0.1:8000/api/v1/devices/
```
