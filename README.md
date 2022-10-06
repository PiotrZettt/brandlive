# brandlive
Brandlive is a simple user profile platform where people can register their interst of working for a marketing agency.

You will nedd an admin account: python manage.py createsuperuser

# How to run:
To run this app you will need python3 installed on tour system.
Create a new folder for the application:
```mkdir <folder_name> && cd <folder_name>```
Clone the git repo:
```git clone git@github.com:PiotrZettt/brandlive.git```
Create a virtual environment for the project:
```python3 -m venv <your env name>```
Change directory to the brandlive Django app:
```cd brandlive```
Before you create a database and run the server you will need to create a secret key by exporting an environmental variable. It will be read and used by Django's settings.py
```export SECRET_KEY="<Use a string here>"```
We can create a database now:
```python manage.py makemigrations
python manage.py migrate```

You will also need an admin account. Use command:
```python manage.py createsuperuser```
and follow the prompts.

Everythings ready now. Run the app by:
```python manage.py runserver```


Demo: https://brandlive.herokuapp.com
