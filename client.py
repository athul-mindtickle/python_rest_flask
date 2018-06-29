from flask import Flask, request
from flask_restful import Api, Resource
from json import dumps
from flask import jsonify
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class User_ID(Resource):

    def get(self):
        User_Ser_count = pd.read_csv('/Users/athul/Desktop/linkedin.mindtickle.com_Series_count_sorted.csv')
        out = {'distinctid': str(request.args['distinctid'])}  # Fetches first column that is Employee ID
        distinct_id = out ['distinctid']
        out['Series'] = User_Ser_count.loc[User_Ser_count['distinctid'] == distinct_id]['SeriesId'].values.tolist()
        print(type(out['Series']))
        return jsonify(out)


api.add_resource(User_ID, '/userid')  # Route_1


if __name__ == '__main__':

    app.run(port='5002',debug=True)
