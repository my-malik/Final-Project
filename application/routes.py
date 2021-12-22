from flask import render_template, request, redirect, url_for 
from application import app, db
from application.models import Players
from application.forms import Player_nameForm

@app.route('/')
def home():
    all_players = Players.query.all()  #retreives list of players from db 
    return render_template("index.html", title="Home", all_players=all_players)



@app.route('/create_player', methods=["GET","POST"])
def create_player():
    form = Player_nameForm()

    if request.method == "POST":
        new_player = Players(player_name=form.player_name.data) 
        db.session.add(new_player)
        db.session.commit()
        
        return redirect(url_for("home"))
    return render_template("create_player.html", title="Add a player", form=form)


@app.route('/update_player/<int:id>', methods=["GET","POST"])
def update_player(id):

    form = Player_nameForm()
    player = Players.query.get(id)

    if request.method == "POST":
        player.player_name = form.player_name.data

        db.session.commit()
        
        return redirect(url_for("home"))
    return render_template("update_player.html", player=player, form=form)
    
@app.route('/delete_player/<int:id>')
def delete_player(id):
    player = Players.query.get(id)
    db.session.delete(player)
    db.session.commit()
        
    return redirect(url_for("home"))



        





