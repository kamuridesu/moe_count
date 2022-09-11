from src.db import DB
from src.util import imageBuilder
from src.merge_svg import mergeAllImages
from flask import Flask, request, g, jsonify, Response

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DB("./db/users.db")
    return db


@app.route("/")
def index():
    params = request.args
    if "username" not in params or params.get("username") == "":
        return "Missing username parameter!", 400
    username = params.get("username")
    db = get_db()
    results = db.search(username)
    counter = 0
    if results:
        counter = results[0][1]
        db.addCount(username, counter + 1)
        counter = counter + 1
    else:
        db.addUser(username)
    result = mergeAllImages(imageBuilder(counter))
    return Response(result.getvalue(), mimetype='image/svg+xml', headers={
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Vary': 'Accept-Encoding',
        "Pragma": "no-cache"
        "Expires": "0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
