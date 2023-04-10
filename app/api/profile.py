import json
import time

from flask import request
from flask_restful import Resource
from azure.data.tables import TableServiceClient

# azure-core==1.26.4
# azure-data-tables==12.4.2

with open('profiles.json', 'r') as f:
    db = json.load(f)

class ProfileResource(Resource):
    def get(self):
        return sorted(db, key=lambda k: k['last_name'])
    
    def post(self):
        print("self: ", request.get_json())
        new_dict = request.get_json()
        conn = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=bgtimer;AccountKey=9GB9Uuvf9IjSTSdYOyGu1Soa6klD1ImdzXNvhnyFJsLSKpLoIVfi6ACmt7Ey34uOnDcdoo5oZcOn+AStli9vcQ=="
        service = TableServiceClient.from_connection_string(conn_str=conn)
        from azure.data.tables import TableClient
        my_filter = "PartitionKey eq 'rm1' and RowKey eq '102'"
        table_client = TableClient.from_connection_string(conn_str=conn, table_name="cktest")
        my_entity = {
            u'PartitionKey': new_dict["name"],
            u'RowKey': str(round(time.time(),4)),
            u'PurchaseDate': time.time()
        }
        my_entity2 = {
            u'PartitionKey': new_dict["name"],
            u'RowKey': str(round(time.time(),4)),
            u'PurchaseDate': time.time()
        }
        entity = table_client.create_entity(entity=my_entity)
        print("tm", round(time.time(), 4))
        try:
            entity = table_client.create_entity(entity=my_entity2)

        except:
            my_entity2['RowKey'] = str(round(float(my_entity2['RowKey']) + 0.0001, 4))
            entity = table_client.create_entity(entity=my_entity2)
        # entities = table_client.query_entities(my_filter)
        # return_dict = {}
        # for entity in entities:
        #     for key in entity.keys():
        #         # return_dict[key]=entity[key]
        #         print("Key: {}, Value: {}".format(key, entity[key]))
        return {"a":"b"}