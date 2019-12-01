<h1 align="center">RESTful API for Udacity trivia application :trophy:</h1>
<p>
  <img src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/wanderindev/trivia-api/blob/master/README.md">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/trivia-api/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://htmlpreview.github.io/?https://github.com/wanderindev/trivia-api/blob/master/backend/htmlcov/index.html">
    <img alt="Coverage" src="https://img.shields.io/badge/coverage-99%25-yellowgreen.svg" target="_blank" />
  </a>  
  <a href="https://github.com/wanderindev/trivia-api/blob/master/LICENSE.md">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/JavierFeliuA">
    <img alt="Twitter: JavierFeliuA" src="https://img.shields.io/twitter/follow/JavierFeliuA.svg?style=social" target="_blank" />
  </a>
</p>

>Triva API is the second project for the 2019 Udacity Full-stack Developer Nanodegree.  The project is
>associated with the _API Development and Documentation_ course.  Visit 
>[this repository](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter) 
>for the starter code and project instructions.

## Project overview
The project contains a working frontend and a starter code for a backend.

The work performed on the frontend was limited to adding CSS to improve the application look and feel,
fixing inconsistent indentation, removing unnecessary returns, adding alt attributes to images, and fixing
the number of arguments in some function signatures.

In the backend, I added all the endpoints required by the frontend, completed the SQLAlchemy models,
and added automated tests.

## How to use
**Note:** A 2-minute video showing all the steps below is available [here]()

To complete the steps, you need three terminal windows:  one for running
the frontend, one for running the database, and one for running the backend.

### Clone the repository
In the first terminal window, clone the repository and cd into the project root:
```sh
git clone https://github.com/wanderindev/trivia-api.git
cd trivia-api
``` 

### The database
I included a Dockerfile and a docker-compose.yml that runs a Postgresql instance,
creates two databases (one for development and one for testing), and adds mock data
to the development database.  

If you have Docker installed and configured in your system, this is the 
recommended way for running the database.  Otherwise, create and initialize 
the databases in your own Postgresql instance and adjust
the connection string in ```config.py```.

To use the included Postgresql setup, cd into the backend directory 
and run docker-compose:
```sh
cd backend
docker-compose up --build
```

### The backend
In the second terminal window, cd into the project root, create a virtual
environment, and activate it:
```sh
cd trivia-api
python3 -m venv venv
. venv/bin/activate
```
Install the project requirements:
```sh
cd backend
pip install -r requirements.txt
```

To run the tests, use:
```sh
coverage run -m unittest tests/system_tests.py tests/integration_tests.py tests/unit_tests.py
```

To run the RESTful API, use:
```sh
export FLASK_APP=run
flask run
```
With the API running, you can connect to the different endpoint using the
included Postman collection (```trivia_api.postman_collection```) or running
the frontend.

### The frontend
In the third terminal window, cd into frontend directory:
```sh
cd trivia-api/frontend
``` 

Install the project dependencies:
```sh
npm install
```

Start the frontend:
```sh
npm start
```

## API documentation
For additional information about the API endpoints, visit the 
[API documentation](https://documenter.getpostman.com/view/2325066/SWDze1MH).

## References
[_Effective Python_](https://www.amazon.com/-/es/Brett-Slatkin/dp/0134034287/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=effective+python&qid=1574387968&sr=8-3) by Brett Slatkin

[_Flask Web Development_](https://www.amazon.com/-/es/Miguel-Grinberg/dp/1491991739/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3JY2ISKWMZ13V&keywords=flask+web+development&qid=1574388048&sprefix=flask+web+de%2Caps%2C208&sr=8-3) by Miguel Grinberg

[_Essential SQLAlchemy_](https://www.amazon.com/-/es/Jason-Myers/dp/149191646X/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2S93O5UCTEF4F&keywords=essential+sqlalchemy&qid=1574388098&sprefix=essential+sqlal%2Caps%2C203&sr=8-1) by Jason Myers and Rick Copeland

[_Quickly Create Custom API Documentation_](https://www.getpostman.com/api-documentation-generator)

[_Example Google Style Python Docstrings_](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

 ## Author

👤 **Javier Feliu**

* Twitter: [@JavierFeliuA](https://twitter.com/JavierFeliuA)
* Github: [@wanderindev](https://github.com/wanderindev)

[Starter code](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter) 
provided by [Udacity](https://www.udacity.com/).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Javier Feliu](https://github.com/wanderindev).<br />

This project is [MIT](https://github.com/wanderindev/trivia-api/blob/master/LICENSE.md) licensed.

***
_I based this README on a template generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_