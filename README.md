g3kko-engine
============

Engine to calculate return of investments using Python with Flask and SQLAlchemy.

Getting started
---------------
Checkout this project and use [pipenv](https://docs.pipenv.org). Follow the example [workflow](https://docs.pipenv.org/basics/#example-pipenv-workflow).

Install dependencies

    pipenv install

Use the shell to execute something

    pipenv shell


Run the engine
--------------

Start server on local host (port 5000)

    pipenv shell
    export FLASK_APP=g3kko/engine.py
    flask run

Development
-----------

Install a new module

    pipenv install <module>

Create a Pipfile.lock from the installed versions

    pipenv lock
