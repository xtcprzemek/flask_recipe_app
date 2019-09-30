from project import db


class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(64), index=True, unique=True)
    recipe_descr = db.Column(db.String(128))
