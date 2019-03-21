
from flask_wtf import FlaskForm
from wtforms.fields import StringField  , SubmitField , TextAreaField 
from wtforms.validators import DataRequired 

class CategoryForm(FlaskForm):
    name= StringField('Category name' , validators = [DataRequired()] )
    description=TextAreaField('Category description', validators = [DataRequired()])
    submit= SubmitField('submit' )

