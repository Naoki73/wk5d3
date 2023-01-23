from flask import Flask, redirect, url_for, render_template, request
import requests as r
from app import app
from app.findpoke import findpokemon
from .models import Pokemon



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=["GET", "POST"])
def pokemon():
    if request.method == "POST":
        name = addpokemon.name.data
        ability = addpokemon.ability.data
        Front_Shiny = addpokemon.Front_Shiny.data
        Base_ATK = addpokemon.Base_ATK.data
        Base_HP = addpokemon.Base_HP.data
        Base_DEF = addpokemon.Base_DEF.data

        print(name, ability, Front_Shiny, Base_ATK, Base_HP, Base_DEF)

        pokemon = Pokemon(name, ability, Front_Shiny, Base_ATK, Base_HP, Base_DEF)
        print(pokemon)

        pokemon.saveToDB()
        
        pokemon_name = request.form["pokemon_name"]
        pokemon_data = findpokemon(pokemon_name)
        return render_template("pokemon_data.html", pokemon_data = pokemon_data)
    else:
        return render_template("pokemon.html")

