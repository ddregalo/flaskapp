import pytest
from app import create_app
from flask import(
    Flask,
    url_for
)

def test_app_index_status_ok(client):
    assert client.get(url_for('index')).status_code == 200

def test_app_index_page_title(client):
    response = client.get('/')
    assert b'CHATTER' in response.data
