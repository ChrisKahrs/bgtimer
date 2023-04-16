from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
import json
import time
from azure.data.tables import TableServiceClient
from azure.data.tables import TableClient

from .profiles import profiles_blueprint
from .api.profile import ProfileResource

app = Flask(__name__)
api = Api(app, prefix= '/api')

app.register_blueprint(profiles_blueprint)

api.add_resource(ProfileResource, '/profiles')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_form', methods=['GET', 'POST'])
def read_form():    
    data = request.form
    # if reset, then delete that section of table
    # if not then add "start_game" to table
    game_start_time = round(time.time(),4)
    conn = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=bgtimer;AccountKey=9GB9Uuvf9IjSTSdYOyGu1Soa6klD1ImdzXNvhnyFJsLSKpLoIVfi6ACmt7Ey34uOnDcdoo5oZcOn+AStli9vcQ=="
    table_client = TableClient.from_connection_string(conn_str=conn, table_name="cktest")
    my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time),
            u'Status': "start_game"
        }
    table_client.create_entity(entity=my_entity)
    # add pause player
    my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0001),
            u'Player': 'pause_player',
            u'Player_Color': 'black',
            u'Status': "pause_player_added"
        }
    table_client.create_entity(entity=my_entity)
    # add each player to the table with current start time
    if data['player_1_color'] != 'none':
        my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0002),
            u'Player': 'player_1',
            u'Player_Color': data['player_1_color'],
            u'Status': "player_1_added"
        }
        table_client.create_entity(entity=my_entity)
    if data['player_2_color'] != 'none':
        my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0003),
            u'Player': 'player_2',
            u'Player_Color': data['player_2_color'],
            u'Status': "player_2_added"
        }
        table_client.create_entity(entity=my_entity)
    if data['player_3_color'] != 'none':
        my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0004),
            u'Player': 'player_3',
            u'Player_Color': data['player_3_color'],
            u'Status': "player_3_added"
        }
        table_client.create_entity(entity=my_entity)    
    if data['player_4_color'] != 'none':
        my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0005),
            u'Player': 'player_4',
            u'Player_Color': data['player_4_color'],
            u'Status': "player_4_added"
        }
        table_client.create_entity(entity=my_entity)
    if data['player_5_color'] != 'none':
        my_entity = {
            u'PartitionKey': data['roomname'],
            u'RowKey': str(game_start_time+0.0006),
            u'Player': 'player_5',
            u'Player_Color': data['player_5_color'],
            u'Status': "player_5_added"
        }
        table_client.create_entity(entity=my_entity)
    return render_template('index2.html', k=data)

@app.route('/status_form', methods=['GET', 'POST'])
def status_form():
    data = request.form
    