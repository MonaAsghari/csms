## Quick start for beginning
![has_to_be](./resources/img/has_to_be.png?raw=true)


# Project Name
  - A CSMS (charging station management system)
# Project Description
  
- A CSMS for calculating the total price of charging process rating.
Rating is the process of applying a rate to a CDR(charge detail record).
  
# Setup
1.The first thing to do is to clone the repository:
  
    $ git clone https://github.com/MonaAsghari/csms.git
    $ cd csms
  
2.Create a virtual environment to install dependencies in and activate it:

    $ python3 -m venv project-name
    $ project-name\Scripts\activate.bat

3.Then install the dependencies:
  
    (venv)$ pip install -r requirements.txt

4.Once pip has finished downloading the dependencies you should do the local configs:
  
  - First, rename the file `.env.example` to `.env` and set your own config settings.
  - Generate a KEY from the link below and put it on `.env` file as SECRET_KEY value
  
        https://django-secret-key-generator.netlify.app/
  
  - here is where you place your `DEBUG=True` or `DEBUG=False`setting

5.Now you can run the project: 

    (venv)$ cd project
    (venv)$ python manage.py runserver

6.And navigate to http://127.0.0.1:8000/

- You can test API in the swagger or in postman platform.
- There is a sample API testing in the `docs` folder of project which you can import it in postman platform.

# Tests
To run the tests, cd into the directory where manage.py is:

    (venv)$ python manage.py test app-name.tests.test_name

# Deployment
1.To build an image based on docker, follow steps below in terminal:

    (venv)$ docker-compose up -d
    (venv)$ docker ps -a
    (venv)$ docker logs csms_api

2.Then navigate to http://127.0.0.1:8000/ in your browser

# Load Docker Image
If there is an image file of project, run this command in your terminal:

    (venv)$ docker load image-name 
