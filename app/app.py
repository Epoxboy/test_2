import json
import os
from flask import Response
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

f= open("commithash","r")
commit_sha = f.read().replace('\n','')

js = {
 "version": "1.0",
 "description" : "pre-interview technical test",
 "lastcommitsha": commit_sha
 }

class Healthcheck(Resource):
    def get(self):
        return Response(json.dumps(js),  mimetype='application/json')

api.add_resource(Healthcheck, '/healthcheck')

app.run(host="0.0.0.0", port=int("5008"), debug=True)
