"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = [
    'oh-so-meh', 'underwhelming', 'sleep-inducing', 'deeply confused in ways I can\'t begin to understand']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
      </head>

      <body>
        <h1>Hi! This is the home page.</h1>
        <li><a href="/hello">Submit Name</a>
      </body>
    </html>
    """



@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <br>
            <input type="radio" name="compliment" value='awesome'>awesome
            <input type="radio" name="compliment" value='terrific'>terrific
            <input type="radio" name="compliment" value='fantastic'>fantastic
            <input type="radio" name="compliment" value='neato'>neato
            <input type="radio" name="compliment" value='fantabulous'>fantabulous
            <input type="radio" name="compliment" value='wowza'>wowza
            <input type="radio" name="compliment" value='oh-so-not-meh'>oh-so-not-meh
            <br>
            <input type="radio" name="compliment" value='brilliant'>brilliant
            <input type="radio" name="compliment" value='ducky'>ducky
            <input type="radio" name="compliment" value='coolio'>coolio
            <input type="radio" name="compliment" value='incredible'>incredible
            <input type="radio" name="compliment" value='wonderful'>wonderful
            <input type="radio" name="compliment" value='smashing'>smashing
            <input type="radio" name="compliment" value='lovely'>lovely
            <br><br>
            <input type="submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def say_diss():
    """Says diss"""

    insult = choice(DISS)
    return """

    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
