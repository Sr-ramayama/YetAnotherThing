#!/bin/sh
export FLASK_APP=./ToDo/endpoint.py
pipenv run flask --debug run -h 0.0.0.0