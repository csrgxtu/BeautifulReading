from flask import Flask
import pyorient
# connect to orientdb
orientClient = pyorient.OrientDB("192.168.100.2", 2424)
orientSession = orientClient.connect( "root", "archer" )
orientClient.db_open('bookshelf', "root", "archer" )
app = Flask(__name__)

@app.route("/similiar/<user_id>")
def hello(user_id):
    # first, get my own book list
    cmd = 'select expand(out(UserHasBook)) from User where user_id="' + user_id + '"'
    result = orientClient.query(cmd, 10, '*:0')
    print result[0]
    print type(result[0])
    return user_id

if __name__ == "__main__":
    app.run(port=9100)
