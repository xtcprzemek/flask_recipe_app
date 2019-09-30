# project/recipes/views.py

#################
#### imports ###m models import Users
#################

from flask import render_template, Blueprint
from .models import Recipe

################
#### config ####
################

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')


################
#### routes ####
################

@recipes_blueprint.route('/')
def index():
    recipes = Recipe.query.all()
    print(recipes[0].recipe_name)
    return render_template('recipes.html')
