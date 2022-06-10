from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    game_info = {"gameId": game_id, "board": game.board}

    return jsonify(game_info)
    #check jsonify method
    # will need to make sure the route stores
    # the new game in the games dictionary

@app.post('/api/score-word')
def score_word():
    '''takes in a played word, tests if it is valid and return score'''
    #find the game object in the games dict that matches the game id
    #once we have that object stored as a variable we will call
    #boggle methods to test and score word

    gameId = request.json["gameId"]
    word = request.json['word']
    breakpoint()
    game = games[gameId]
    if not game.is_word_in_word_list(word):
        return jsonify({result: "not-word"})
    elif not game.check_word_on_board(word):
        return jsonify({result: "not-on-board"})
    else:
        return jsonify({result: "ok"})

