# Server Application

## Models

- Entities
  - User (django default)
    - user_id (pk)
    - username
    - email
    - password
    - role                      # set of permissions
  - Log
    - log_id (pk)
    - log_level
    - message
    - created_at
    - device_id (fk)
  - Device
    - device_id (pk)
    - device_name
    - device_type
    - os_version
    - user_id (fk)              # device_user
  - Application
    - app_id (pk)
    - app_name
    - package_name
    - version
    - policy

## How to Run

```shell
pythone manage.py runserver <ip>:<port>
```

## How Setup from first

1. virtual environment

    ```shell
    python3 -m venv myenv
    source myenv/bin/activate
    ```

2. install django

    ```shell
    pip install django djangorestframework
    ```

3. start django project

    ```shell
    django-admin startproject config . 
    ```

4. start api app

    ```shell
    python3 manage.py startapp api 
    ```

5. migration

    ```shell
    python3 manage.py migrate
    ```

6. create superuser

    ```shell
    python3 manage.py createsuperuser

    Username: abbas
    Email address: abbas.yazdanmehr1@gmail.com
    Password: 1
    ```

7. run server

    ```shell
    python3 manage.py runserver
    ```

8. after adding each model

    ```shell
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
