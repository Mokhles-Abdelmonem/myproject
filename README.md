# myproject
download python from :https://www.python.org/downloads/
install python  Make sure you select the Install launcher for all users and Add Python to PATH checkboxes.
Verify Python Was Installed On Windows  py opening command prompt and type 
...\>python.
you should see python version, date and other informations

Verify Pip Was Installed :
Enter ...\>pip -V in the command prompt.
If Pip was installed successfully, you should see pip virsion ,path to folder location and python version 
If your version of Python is missing Pip you should see :
('pip' is not recognized as an internal or external command,Operable program or batch file.) so follow the steps on https://phoenixnap.com/kb/install-pip-windows

Install virtualnv:
Type the following pip command in the console
...\> pip install virtualenv
after installation

Setting up a virtual environment:
...\> py -m venv virtual-name

move project files in the virtual environment folder

activate the environment:
...\> virtual-environment-name\Scripts\activate.bat
to make sure its activated you should see (virtual-environment-name) befor bath like this:
(virtual-name)...\>

Install django:
(virtual-name)...\> py -m pip install Django
after installation

show the Packages that installed in your invironment
(virtual-name)...\>pip list
if any of the following Packages not installed on your virsion , make sure to install it :
Package             Version
------------------- -------
asgiref             3.5.0
beautifulsoup4      4.10.0
Django              4.0.1
django-bootstrap4   21.2
django-crispy-forms 1.14.0
Pillow              9.0.0
pip                 21.3.1
setuptools          60.2.0
soupsieve           2.3.1
sqlparse            0.4.2
tzdata              2021.5
wheel               0.37.1

by the following command :
(virtual-name)...\>pip install the-name-of-the-Package
example: 
(virtual-name)...\>pip install Pillow

after installing all 
change directory to the project7
(virtual-name)...\>cd project7
now you are ready to run the server 
(virtual-name)...\>python manage.py runserver
you should see :


System check identified no issues (0 silenced).
February 01, 2022 - 15:38:40
Django version 4.0.1, using settings 'project7.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


open your browser go to http://127.0.0.1:8000/
now you can use the server 
register , login , search , reset password by mail , change profile settings
