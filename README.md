# brandlive
Brandlive is a simple user profile platform where people can register their interst of working for a marketing agency.

You will nedd an admin account: python manage.py createsuperuser

# How to run:
To run this app you will need python3.10 installed on your system.  

Create a new folder for the application and move into that folder:  

```mkdir <folder_name> && cd <folder_name>```  

Clone the git repo:  

```git clone git@github.com:PiotrZettt/brandlive.git```  

Create a virtual environment for the project:  

```python3 -m venv <your_env_name>```  

Activate your envirenment by:
```source venv/bin/activate```

Change directory to the brandlive Django app:  

```cd brandlive```  

Install all requirements by:  
```pip install -r requirements.txt```

Before you create a database and run the server you will need to create a secret key by declaring an environmental variable. It will be read and used by Django's settings.py  

```export SECRET_KEY="<Use_a_string_here>"```  
You will have to do it each time you start a new Terminal/Comand Line session.

We can create a database now:  

```python manage.py makemigrations```  
```python manage.py migrate```  

You will also need an admin account. Use command:  

```python manage.py createsuperuser```  

and follow the prompts.  
Everything's ready now. Run the app by:  

```python manage.py runserver```

The app should open in your browser on http://127.0.0.1:8000/


Demo: https://brandlive.herokuapp.com
