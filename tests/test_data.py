import pytest
from splinter import Browser
from data import Articles
from app import create_app
from flask import(
    Flask,
    url_for
)

class TestData():

    def test_data_articles(self):
        assert Articles() == [
            {
                'id': 1,
                'title': 'Practising Python with Flask',
                'body': 'This was a very hard process and required a lot of research and baby steps. It was challenging to write tests using pytest.',
                'author': 'Daniel Campos',
                'create_date': '05-06-2018'
            },
            {
                'id': 2,
                'title': 'Practising Python with Flask 2',
                'body': 'This was a very hard process and required a lot of research and baby steps. It was challenging to write tests using pytest.',
                'author': 'Daniel Campos',
                'create_date': '05-07-2018'
            },
            {
                'id': 3,
                'title': 'Practising Python with Flask 3',
                'body': 'This was a very hard process and required a lot of research and baby steps. It was challenging to write tests using pytest.',
                'author': 'Daniel Campos',
                'create_date': '05-07-2018'
            }
        ]
