from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Player_nameForm(FlaskForm):
    player_name = StringField("Player name", validators=[DataRequired()])
    # position = StringField("Position", validators=[DataRequired()])
    submit = SubmitField("Add player")