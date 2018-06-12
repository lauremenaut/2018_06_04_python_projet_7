from flask_wtf import FlaskForm

from wtforms import TextAreaField

class QueryForm(FlaskForm):
    query = TextAreaField("Saisissez ici votre question pour GrandPy Bot :")
