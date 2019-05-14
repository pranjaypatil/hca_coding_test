# HCA Coding Test
## Description
This repository contains the code for HCA coding challenge. It is a web app created using the Django framework https://www.djangoproject.com/.

## System Requirements
To build this app, following componenets are required,
* Python 3.5+
* Django 2.1+

## How to run
Clone the repository from Github and run 
`django-admin manage.py migrate` This will create the required database and tables. Currently, this app uses Sqllite3 database.

To run the server use `django-admin manage.py runserver <optional address e.g. localhost:8000>`
This command needs to be run from the directory containing the manage.py script. It is located in hca_database_file directory.

Navigate to localhost:8000/hcaapp (if that is used in earlier step) from a web browser. The website provides a place to upload the TSV file.

The user is provided with an option to overwrite the exisiting records in the table, select this checkbox if you wish to truncate the table before adding new records.

The upload button will send the file to the server and the server responds with the total revenue of **all the records in the table**.

Also test out the functionality when no file is uploaded or the uploaded file is having improper TSV format.

## Avoid the trouble to setup the project!
This app is live [here](http://pranjay.pythonanywhere.com/hcaapp/). Full functionality can be tested by visiting this website.

Thanks!
