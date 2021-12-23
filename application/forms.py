from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Player_nameForm(FlaskForm):
    player_name = StringField("Player name:", validators=[DataRequired()])
    position = SelectField("Position:", 
        choices=[ 
            ('Goalkeeper','GK'),
            ('Defender','DEF'),
            ('Midfielder','MID'),
            ('Striker','ST')
        ]
    )
    team = SelectField("Team:", 
        choices=[ 
            ('ManU','ManU'),
            ('City','City')

        ]
    )
    submit = SubmitField("Add player")