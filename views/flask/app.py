import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("stats.html")

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template("notfound.html")
