from flask import Flask
from random import choice
from flask import jsonify
from BookAPI import BookAPI
from util import ldUserAgents

app = Flask(__name__)

@app.route("/book_api/<isbn>")
def book_api(isbn):
    user_agents = ldUserAgents('./UserAgentString.json')
    b = BookAPI(isbn, choice(user_agents))
    return jsonify(b.api())

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=7000)
