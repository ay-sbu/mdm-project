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
curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNTM2MjI4LCJpYXQiOjE3MjI1MzU5MjgsImp0aSI6IjNiN2JjNzliZWM1ZTQzODE4ODM3OTkyZjRmZjE1YTEzIiwidXNlcl9pZCI6MX0.dv3xf2APY3s0mT5JR76j_lP-qpT6mU1OBkeM3u8X-Hk' -i http://127.0.0.1:8000/api/v1/devices/
```
