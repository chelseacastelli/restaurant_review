
from app import app, db
from models import *
from forms import *

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('landing_page.html', restaurants=restaurants)



