import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/grafana', methods=['GET'])
def home_grafana():
    resp = flask.make_response()
    template = "<h1>Distant Reading Archive</h1><p>This is a check for nested cookie</p>"
    resp = flask.make_response(template)
    return resp

#@app.route('/get-cookie/')
#def get_cookie():
#    username = request.cookies.get('name')

@app.route('/', methods=['GET'])
def home():
    template = "<h1>Distant Reading Archive</h1><a href=http://127.0.0.1:5000/grafana>Visit grafana</a><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    resp = flask.make_response(template)
    resp.set_cookie("root", "root-cookie", path="/")
    resp.set_cookie("root-grafana", "root-grafana-cookie", path="/grafana")
    return resp

app.run()
