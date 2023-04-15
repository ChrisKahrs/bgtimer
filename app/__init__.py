from flask import Flask, render_template, request
from flask_restful import Api

from .profiles import profiles_blueprint
from .api.profile import ProfileResource

app = Flask(__name__)
api = Api(app, prefix= '/api')

app.register_blueprint(profiles_blueprint)

api.add_resource(ProfileResource, '/profiles')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read_form', methods=['GET', 'POST'])
def read_form():
    data = request.form
    x = data['gamename']
    print("data_room: ",x)
    return render_template('index2.html')