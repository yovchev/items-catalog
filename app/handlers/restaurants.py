from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session

restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/')
@restaurants.route('/restaurants/')
def restaurant():
	#return current_app.template_folder
	return render_template('restaurants.html', name=current_app.name)
