[![Build Status](https://travis-ci.org/RachealN/IReporter-3.svg?branch=develop)](https://travis-ci.org/RachealN/IReporter-3)
[![Coverage Status](https://coveralls.io/repos/github/RachealN/IReporter-3/badge.svg?branch=develop)](https://coveralls.io/github/RachealN/IReporter-3?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/9af5ddd03ddedb899317/maintainability)](https://codeclimate.com/github/RachealN/IReporter-3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9af5ddd03ddedb899317/test_coverage)](https://codeclimate.com/github/RachealN/IReporter-3/test_coverage)

# IReporter-3

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

# Getting Started

Clone the project to your computer using this command

```git clone(https://github.com/RachealN/IReporter-3.git)```

# Preprequisites
Make sure you python3 and postman installed on your computer.

```Install python```

```Install postman```

```Vs Code```   or any other text editor of your choice

# create a virtual environment
work in the virtual environment. Below is a command on how to create virtual environment for windows

```virtualenv venv ```

# Activate the virtaul environment 
By running this command 
```cd venv/scripts/activate```

# Install the dependencies in the requirements.txt file using pip
```pip install -r requirements.txt```

# Running the project

To run this project

Navigate to the directory where the project was cloned and run this command

```python run.py```

# Project link

https://github.com/RachealN/i-Reporter-API/tree/develop

# Features

○	Create/Register user

○	Post Login user

○	Get a specific intervention record

○	Get all intervention records

○	Get all intervention record of a user

○	Create/Post intervention record

○	Patch intervention record's status

○	Patch redflag record's status

○	Patch intervention record by location

○	Patch intervention record by comment

○	Delete Intervention record

○	Update intervention record

○	create/Post redflag record

○	Get all redflag records

○	Get all redflags by a user

○	Get a specific redflag record

○	Patch redflag record by location

○	Patch redflag record by comment

○	Delete redflag record

○	Update redflag record





# API Endpoints

| Methods | Endpoints           |Functionality|
----------|---------------------|-------------------------------|
|  POST| /api/v1/red-flags   |  Create a red-flag            ||          
|  GET | /api/v1/red-flags    |  Get all redflags            ||          
   GET | /api/v1/red-flags/1    | Get a single redflag        | |          
|  PATCH  | /api/v1/red-flags/1/comment    |  Update comment   | |           
|  PATCH  | /api/v1/red-flags/1/location    |  Update location | |           
|  DELETE  |/api/v1/red-flags/1   |  Delete a redflag          | |   
|  UPDATE  |/api/v1/red-flags/1   |  Update a redflag          | |          
|  POST  |/api/v1/auth/register   |  register a user |              ||           
|  POST  |/api/v1/auth/login   | login a user |                     ||            
|  GET  |/api/v1/intervention    |  Get all intervention record's |                    ||           
|  GET  |/api/v1/intervention/1   |  Get a single intervention record |              | |            
|  DELETE  |/api/v1/intervention/1   |  Delete intervention record |               |
|  POST| /api/v1/intervention    |  Create an intervention record           ||                 
|  PATCH  | /api/v1/intervention/1/comment    |  Update comment   | |           
|  PATCH  | /api/v1/intervention/1/location    |  Update location | |           
|  DELETE  |/api/v1/intervention/1   |  Delete intervention         | |           
|  PATCH  |/api/v1/intervention/1/status   |  Update intervention status |              ||           
|  PATCH  |/api/v1/redflag/1/status   | upadte redflag status |                     ||            
|  UPDATE  |/api/v1/intervention/1   |  Update intervention record |                    ||           
|               |
 

# How to run tests

Run this command

```py.test --cov=app tests/```

or this to run tests without coverage

```pytest```

#Link to Heroku




# Author

Namaara Racheal

# Licencing

The app is opensource hence free to all users


