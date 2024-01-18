from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja, dojo # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller
@app.route('/ninjas')
def create_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos=dojos)

# Read Users Controller

@app.post('/ninjas/create')
def add_ninja():
    ninja.Ninja.create_ninja(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojos/{dojo_id}')

# update Users Controller


@app.route('/ninjas/edit/<int:ninja_id>')
def edit_this_ninja(ninja_id):
    ninja_data = ninja.Ninja.edit_ninja(ninja_id)
    return render_template('editninja.html', ninja=ninja_data)

@app.post('/ninjas/edit')
def update_ninja_info():
    ninja.Ninja.update_ninja_info(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojos/{dojo_id}')

# Delete Users Controller

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_ninja(ninja_id):
    ninja.Ninja.delete_ninja(ninja_id)
    return redirect('/dojos')

# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.