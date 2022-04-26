
from app import app, db, login_manager
from models import *
from forms import *
from helper import calculate_average_rating

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


# helper function -- loads user
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=["GET", "POST"])
def login():
    # Check if current_user logged in, if so, redirect to a page that makes sense (index)
    if current_user.is_authenticated:
        flash('You are already logged in, {}!'.format(current_user.username))
        return redirect(url_for('index'))

    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        
        else:
            flash('Incorrect crendetials. Please try again.')
            return redirect('login')

    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():

    # Check if current_user logged in, if so, redirect to a page that makes sense (index)
    if current_user.is_authenticated:
        flash('You are already logged in, {}!'.format(current_user.username))
        return redirect(url_for('index'))
    
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():

        if User.is_user_name_taken(form.username.data):
            flash('Username taken')
            return redirect(url_for('register'))
        
        if User.is_email_taken(form.email.data):
            flash('There is already an account associated with this email')
            return redirect(url_for('login'))
           
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered.')
        login_user(user)
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))


@app.route('/user/<username>', methods=["GET", "POST"])
@login_required
def user(username):
    form = NewRestaurantForm(csrf_enabled=False)

    if form.validate_on_submit():
        new_rest = Restaurant(name=form.name.data, address=form.address.data, cuisine=form.cuisine.data, num_reviews=0, avg_rating=0)
        db.session.add(new_rest)
        db.session.commit()
        return redirect(url_for('user', username=username))

    restaurants = Restaurant.query.all()
    return render_template('user.html', restaurants=restaurants, form=form)


@app.route('/reviews/<int:restaurant_id>', methods=["GET", "POST"])
def reviews(restaurant_id):
    rest = Restaurant.query.filter_by(id=restaurant_id).first_or_404(description="There is no restaurant with this ID.")
    form = ReviewForm(csrf_enabled=False)

    if form.validate_on_submit():
        if current_user.is_authenticated:
            if int(form.rating.data) < 1 or int(form.rating.data) > 5:
                flash('Please give a rating of 1 to 5 stars.')
                return redirect(url_for('reviews', restaurant_id=restaurant_id))

            new_review = Review(rating=int(form.rating.data), text=form.review.data, restaurant_id=restaurant_id, reviewer_id=current_user.id)
            db.session.add(new_review)

            rest.num_reviews += 1
            rest.avg_rating = round(calculate_average_rating(rest))

            db.session.commit()

            return redirect(url_for('reviews', restaurant_id=restaurant_id))

        else:
            flash('Please log in or create an account to leave a review.')
            return redirect(url_for('reviews', restaurant_id=restaurant_id))

    return render_template('review.html', restaurant=rest, form=form)


@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('landing_page.html', restaurants=restaurants)