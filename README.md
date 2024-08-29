# MYREADAPP REST API

These steps below is only when you have cloned the repo.

## **STEP 1**

After, you need to go to  **`myreadapp-rest-api`** folder.

- With the command:

```bash
cd myreadapp-rest-api
```

## **STEP 2**

Create virtual environment with **`venv`**.

- With the command:
```bash
python3 -m venv .venv --prompt myreadapp-rest-api
```

Activate **`venv`**

- With the command:

```bash
source .venv/bin/activate
```

## **STEP 3**

Install requirements.

- With the command:

```bash
make dev-install
```


## **STEP 4**

Create **`.env`** file

- With the command

```bash
nano .env
```
Copy and paste the information below inside the file **`.env`**.

```bash
SECRET_KEY=      # <-- Django SECRET_KEY goes here
DB_NAME=        # <-- PorsgreSQL DB_NAME (database name) goes here
DB_USER=postgres     # <-- PorsgreSQL default username (you can change it however you want) 
DB_PWD=postgres       # <-- PorsgreSQL default password (you can change it however you want) 
DB_PORT=5432
DB_HOST=localhost
```
Your may  want to generate your own `SECRET_KEY` you can either run below command in **`iPython`**

```py
import secrets

secrets.token_urlsafe(50)
```

or by running the script in **`generateSKEY.py`** file.

- With the command 

```bash
python3 -m generateSKEY
```

## **STEP 5**

For the **`DB_NAME`**, I you haven't create database in your PostgreSQL with the name `myreadapp_rest_api_db` (or something else you desire ).
your can do so,

- With the command

```bash
python3 -m createDB
```

or by going to PostgreSQL shell directly

- With the command

```bash
psql -U postgres
```

and enter the query below

```sql
CREATE DATABASE myreadapp_rest_api_db;
```

also if we need to create new user with the name  `myreadapp_rest_api_user`, type in the query below

```sql
CREATE ROLE myreadapp_rest_api_user WITH LOGIN SUPERUSER PASSWORD 'password';
```

And add this information into the **`.env`** file.

## **STEP 6**

After **`.env`** file been setup with the required data, you can migrate the django  project `myreadapp_rest_api`.

- With the command

```bash
make dev-m
```

## **STEP 7**

Insert data to `myreadapp_rest_api_db` database.

- With the command

```bash
make dev-insertdata
```

## **STEP 8**

Create `admin` user account (you can create the name as you desire)

- With the command

```bash
make dev-super
```

## **STEP 9**

Run the django server by running the command below in terminal.

```bash
make
```
