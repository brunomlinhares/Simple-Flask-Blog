from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, BooleanField, SubmitField, validators, SelectField
from blog_app.models.Category import Category


class CategoryCreateAdminForm(FlaskForm):
  

    name = StringField(
        "Name",
        [validators.DataRequired(message="Este campo é obrigatório")],
        name="name",
    )
    parent_id = SelectField("Parent",default=0)
    submit = SubmitField("Submit")
