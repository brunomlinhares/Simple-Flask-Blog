from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField,validators


class PostCreateAdminForm(FlaskForm):
        title = StringField("Title", [validators.DataRequired(message="Este campo é obrigatório")],name="title")
        body = StringField("Body", [validators.DataRequired()],name="body")
        author_id = StringField("Author", [validators.DataRequired()],name="author_id")
        submit = SubmitField("Submit")
        
