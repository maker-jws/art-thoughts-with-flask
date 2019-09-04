from flask import Blueprint
import models
from flask import request
from flask import jsonify
from playhouse.shortcuts import model_to_dict

data = Blueprint("data", "data", url_prefix="/data/v1")


@data.route("/", methods=["GET"])
def get_query_results():
    print('data get route hit')
    return ('hi')
