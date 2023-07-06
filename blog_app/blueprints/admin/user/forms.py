from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField,validators
class UserRegisterAdminForm(FlaskForm):
        name = StringField("Name", [validators.DataRequired(message="Este campo é obrigatório")],name="name")
        email = StringField("Email", [validators.DataRequired()],name="email")
        is_admin = BooleanField("Is Admin")
        submit = SubmitField("Submit")

        
