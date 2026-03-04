# FIDPHA – Django Project

This repository contains a Django project for a pharmacy client fidelisation system
(points by product, contract and sales).

The project is structured to be used both locally and on a server (e.g. PythonAnywhere).

---

## Project structure

```text
FIDPHA_REPO/
├── manage.py
├── requirements.txt
├── fidpha/        # main app
├── polls/         # ignore this
├── site/          # ignore this
├── templates/
├── mysite/        # project settings
└── db.sqlite3     # NOT committed – created after migrate
```


## Create and activate the virtual enviroment 
you need to see somthing like :
(.venv) PS D:\apps_projects\PyCharm_projects\CLONNING_TEST_FIDPHA001>

## Clone the repository

```bash
git clone https://github.com/khalidbrx-Q/FIDPHA_REPO.git
```
Then move into the Django project directory:

(.venv) PS D:\apps_projects\PyCharm_projects\CLONNING_TEST_FIDPHA001> cd FIDPHA_REPO

in this directory you will find manage.py

## Installing requirements 

```bash
pip install -r requirements.txt 
```
like this :
(.venv) PS D:\apps_projects\PyCharm_projects\CLONNING_TEST_FIDPHA001\FIDPHA_REPO> pip install -r requirements.txt 

wait for installing to finish.


## Database initialization 

For now, the SQLite database is not included in the repository.

The database will be created again locally and will be empty.

```bash
python manage.py migrate
```

## Create an admin user 

```bash
python manage.py createsuperuser
```
insert a username, email and password.

## Run server 

```bash
python manage.py runserver
```

open http://127.0.0.1:8000/ in your browser.


## NOTES 


-->Important note about data
Because the database is not committed:
all tables will be created again
there will be no clients, contracts, products or sales by default
You must create your own test data locally (via Django admin or Django shell).


-->Important note about client login
In this project, each client user must be linked to a Client object.
If a user is not linked to a client, the client dashboard will not work.
This is expected behaviour.
