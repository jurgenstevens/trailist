from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

# this form will allow us to get functionality working for create and update
class TrailForm(FlaskForm):
    trail_name = StringField('Trail Name', validators=[DataRequired()])
    distance = IntegerField('Distance', validators=[DataRequired()])
    review = IntegerField('Review', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    trail_image = StringField('Trail Image', validators=[DataRequired()])
    submit = SubmitField('Post')