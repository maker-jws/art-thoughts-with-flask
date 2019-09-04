from flask import Blueprint
import models
from flask import request
from flask import jsonify
from playhouse.shortcuts import model_to_dict

data = Blueprint("data", "data", url_prefix="/data/v1")


@data.route("/", methods=["GET"])
def get_query_results():
    try:
        queries = [model_to_dict(query) for query in models.Data.select()]
        return jsonify(data=queries, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={},
            status={"code": 401,
                    "message": "There was an error getting the resource"},
        )


@data.route('/', methods=["POST"])
def store_query():
    print(request, "request")
    payload = request.form.to_dict()
    print(payload)
    query = models.Data.create(**payload)
    # print(query.___dict___, 'inside query')
    query_dict = model_to_dict(query)
    return jsonify(data=query_dict, status={"code": 201, "message": "Success"})
