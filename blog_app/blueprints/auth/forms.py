from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField,validators
class UserRegisterForm(FlaskForm):
        name = StringField("Name", [validators.DataRequired(message="Este campo é obrigatório")],name="name")
        email = StringField("Email", [validators.DataRequired()],name="email")
        password = StringField("Password", [validators.DataRequired()],name="password")
        submit = SubmitField("Submit")


        
class UserLoginForm(FlaskForm):
        email = StringField("Email", [validators.DataRequired()],name="email")
        submit = SubmitField("Submit")
        password = StringField("Password", [validators.DataRequired()],name="password")

        

        
