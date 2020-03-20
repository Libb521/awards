# Awards

##### Awards is a platform where users can upload  their projects with their project details and have the projects rated and reviewed by other users. a user can also review other people's projects, search for projects and view the project ratings.

## User Stories

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## BDD

| Behavior                          | Input                                   | Output                             |
| --------------------------------- | --------------------------------------- | ---------------------------------- |
| login/sign up                | enter user details                                    | view site             |
| Search for different categories   | project id                             | displays projects of that category   |
| Filter projects   | click a button                          | displays projects |

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python
  - Install and activate virtual
  - Setup Database
  - Install Django
  - Install Postman



### Installation Process
##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```git clone https://github.com/Libb521/awards```.
##### Move to your project directory:
- ```cd Project-Review```.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Install virtual environment using python:
  - ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.6``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After ensuring you have all the above
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.

## Contacts
For further questions you can send an email to eotieno39@yahoo.com

#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)

## Known bugs

No known errors. However, if found, contact me here ## Known bugs

No known errors. However, if found, contact me here 

### Technologies Used
##### Python
##### Django
##### PostgreSQL
##### HTML5
##### CSS3
##### Postman

### Licence
[MIT](LICENSE)