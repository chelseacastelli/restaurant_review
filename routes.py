
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


@app.route('/user', methods=["GET", "POST"])
def user():
    form = NewRestaurantForm(csrf_enabled=False)

    if form.validate_on_submit():
        new_rest = Restaurant(name=form.name.data, address=form.address.data, num_reviews=0, sum_reviews=0, avg_rating=0)
        db.session.add(new_rest)
        db.session.commit()
        return redirect(url_for('user'))

    restaurants = Restaurant.query.all()
    return render_template('user.html', restaurants=restaurants, form=form)


@app.route('/reviews/<int:restaurant_id>')
def reviews(restaurant_id):
    rest = Restaurant.query.filter_by(id=restaurant_id).first_or_404(description="There is no restaurant with this ID.")
    form = ReviewForm(csrf_enabled=False)

    if form.validate_on_submit():
        new_review = Review(rating=int(form.rating.data), text=form.review.data, restaurant_id=restaurant_id, reviewer_id=current_user.id)
        db.session.add(new_review)
        db.session.commit()

        rest.num_reviews += 1
        rest.sum_reviews += new_review.rating
        rest.avg_rating = rest.sum_reviews / rest.num_reviews

    return render_template('review.html', restaurant=rest, form=form)