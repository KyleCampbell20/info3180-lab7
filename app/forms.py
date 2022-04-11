# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import Length, InputRequired, DataRequired

class UploadForm(FlaskForm):
    photo = FileField('Photo ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'])])
    description = TextAreaField('Description',  validators=[DataRequired(),InputRequired(),Length(max=600)])