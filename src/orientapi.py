from flask import Flask
from flask import jsonify
import pyorient
from collections import Counter
# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )
app = Flask(__name__)

@app.route("/similiar/<user_id>")
def hello(user_id):
    # first, get my own book list
    Books = []
    cmd = 'select expand(out(UserHasBook)) from User where user_id="' + user_id + '";'
    result = orientClient.query(cmd)
    for rtv in result:
        Books.append(str(rtv.bid))

    Books = list(set(Books))
    # print Books

    # second, for each book, get user
    User = []
    for book in Books:
        cmd = 'select expand(in(UserHasBook)) from Book where bid="' + book + '"'
        results = orientClient.query(cmd)
        for rtv in results:
            User.append(str(rtv.user_id))
    # print dict(Counter(User).most_common())
    return jsonify(Counter(User).most_common())
    # return user_id

if __name__ == "__main__":
    app.run(port=9100)
