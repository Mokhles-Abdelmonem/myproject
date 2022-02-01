# myproject
the project is a basic web forms 

## Features
- register
- user can login with username or password
- you can search in profiles
- change profile settings
- reset password by mail 


### Server-side

Python 3.6 or higher with the following Packages:

- asgiref
- beautifulsoup4
- Django
- django-bootstrap4
- django-crispy-forms
- Pillow
- pip
- setuptools
- soupsieve
- sqlparse
- tzdata
- wheel

OS support:
- Windows (main). Tested and working on Windows 10


## Installation

- download python from :https://www.python.org/downloads/
- install python  Make sure you select the Install launcher for all users and Add Python to PATH checkboxes.
- Verify Python Was Installed On Windows  py opening command prompt and type 
- ...\>python
- you should see python version, date and other informations

## Setup and run
Verify Pip Was Installed :
Enter ...\>pip -V in the command prompt.
If Pip was installed successfully, you should see pip virsion ,path to folder location and python version 
If your version of Python is missing Pip you should see :
('pip' is not recognized as an internal or external command,Operable program or batch file.) so follow the steps on https://phoenixnap.com/kb/install-pip-windows

### Install virtualnv:
- Type the following pip command in the console
- ...\> pip install virtualenv

### Setting up a virtual environment:
- ...\> py -m venv virtual-name
- move project files in the virtual environment folder

### activate the environment:
- ...\> virtual-environment-name\Scripts\activate.bat
- to make sure its activated you should see (virtual-environment-name) befor bath like this:
- (virtual-name)...\>

### Install django:
- (virtual-name)...\> py -m pip install Django
- after installation

### show the Packages that installed in your invironment:
- (virtual-name)...\>pip list
- if any of the Packages that referred to earlier not installed on your virsion , make sure to install it :

### by the following command :
- (virtual-name)...\>pip install the-name-of-the-Package
example: 
- (virtual-name)...\>pip install Pillow
### run server
- change directory to the project7
- (virtual-name)...\>cd project7
- now you are ready to run the server 
- (virtual-name)...\>python manage.py runserver
- open your browser go to http://127.0.0.1:8000/
- now you can use the server 
- 
### Admin panel
- Admin panel is accessible on admin.html page (e.g. http://127.0.0.1:8000/admin)

## Asking questions
If you have any questions, feel free to ask :
- contact me via email: mokhlesabdelmonem2@gmail.com
- facebook : https://www.facebook.com/mokhles.abdelmonem/
- whatsapp : +20 01144602019

