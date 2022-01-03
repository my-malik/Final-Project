from application import db

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(255), nullable=False)
    players = db.relationship('Players', backref='team', lazy=True)


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(30), nullable=False)
    position = db.Column(db.String(30),nullable=False)  
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)



