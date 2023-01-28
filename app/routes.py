from flask import Flask, redirect, url_for, render_template, request, jsonify
import requests as r
from app import app
from app.services import findpokemon
from .models import Pokemon, User, user_pokedex
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/pokemon', methods=["GET", "POST"])
def pokemon():
    # addpokemon = Pokemon()
    print(request.method)
    if request.method == "POST":
        pokemon_name = request.form['name']
        pokemon_data = findpokemon(pokemon_name)

        new_pokemon = Pokemon(pokemon_data["Name"], pokemon_data["Ability"], pokemon_data["Front_Shiny"], pokemon_data["Base_ATK"], pokemon_data["Base_HP"], pokemon_data["Base_DEF"])
        new_pokemon.saveToDB()

        # if request.form.get('catch'):
        #     pokemon_entry = Pokedex(id=current_user.id, pokemon_id=new_pokemon.pokemon_id)
        #     pokemon_entry.saveToDB()
        #     return redirect(url_for('profile'))



        # pokemon = Pokemon.query.filter_by(name=pokemon_name).first()
        # current_user.catch_pokemon(pokemon)

        return render_template("pokemon_data.html", pokemon_data = pokemon_data)
    else:
        return render_template("pokemon.html")



@app.route("/catch_pokemon", methods=["POST"])
@login_required
def add_to_pokedex():
    
    pokemon_id = request.form['name']
    print("test")

    pokemon = Pokemon.query.filter_by(name=)
    current_user.catch_pokemon(pokemon)

    # pokemon_entry = Pokedex(id=current_user.id, pokemon_id=pokemon.pokemon_id)
    # pokemon_entry.saveToDB()
    



    return redirect(url_for('profile'))


@app.route("/profile")
@login_required
def profile():
    pokedex_entries = user_pokedex.query.filter_by(id=current_user.id).all()
    return render_template("profile.html", pokedex_entries=pokedex_entries)
 