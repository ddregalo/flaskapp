import pytest
from splinter import Browser
from data import Articles
from app import create_app
from flask import(
    Flask,
    url_for
)

Articles = Articles()
browser = Browser()

def test_app_index_status_ok(client):
    assert client.get(url_for('index')).status_code == 200

# Index route tests
def test_app_index_page_navbar(client):
    response = client.get('/')
    assert b'CHATTER' in response.data
    assert b'HOME' in response.data
    assert b'ABOUT' in response.data
    assert b'ARTICLES' in response.data

def test_app_index_page_title(client):
    response = client.get('/')
    assert b'WELCOME TO CHATTER' in response.data

# About route tests
def test_app_about_page_status(client):
    assert client.get('/about').status_code == 200

def test_app_about_page_content(client):
    response = client.get('/about')
    assert b'ABOUT' in response.data
    assert b'Python web app using flask, bootstrap, pytest by Daniel Campos. Create May 2018.' in response.data

# Articles route tests
def test_app_articles_page_status(client):
    assert client.get('/articles').status_code == 200

def test_app_about_page_content(client):
    response = client.get('/articles')
    assert b'ARTICLES' in response.data
    assert b'Welcome to CHATTER articles.' in response.data

# Sinle article view route
def test_single_article_view_status(browser):
    browser.visit('http://localhost:5000/articles')
    link = browser.find_by_tag('li').last
    link.click()
    assert browser.is_text_present('3')
