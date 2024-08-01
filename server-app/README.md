# Server Application

## How Setup?

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
