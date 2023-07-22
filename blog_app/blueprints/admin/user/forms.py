from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField,validators,FileField
class UserRegisterAdminForm(FlaskForm):
        name = StringField("Name", [validators.DataRequired(message="Este campo é obrigatório")],name="name")
        email = StringField("Email", [validators.DataRequired()],name="email")
        profile_image = FileField("Profile Image")
        is_admin = BooleanField("Is Admin")
        submit = SubmitField("Submit")
        password = StringField("Password", [validators.DataRequired()],name="password")

