# Build Python Web Apps with Flask Capstone Project

## The Format
When creating your Flask application, make sure to include the following components.

1. **Routes** — Your application should have at least four distinct routes that each serve their own purpose.

2. **Templates** — Your application should have a base template that is extended to the template files for each of your other routes.

3. **Forms** — Your application should include at least 1 form that collects data from users.

4. **Databases** — Your application should have a SQLite database that has at least three tables storing data. You can implement your database using Flask-SQLAlchemy or by other means if you prefer.

5. **Accounts and Authentication** — Your application should utilize user accounts, require user login to access certain routes, and perform authentication. You can implement your login functionality with Flask-Login or by other means if you prefer.


## Project Objective
A restaurant review site where users can log in/register & either add new locations to the database or leave reviews on existing restaurants.

## Demo It
[Demo](https://murmuring-ocean-09139.herokuapp.com/)


## TODO
- [x] Implement code that handles when the user tries to register but already exists
- [x] Only display the review form when the user is authenticated