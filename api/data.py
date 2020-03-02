from flask import Blueprint
import models
from flask import request
from flask import jsonify
from playhouse.shortcuts import model_to_dict

data = Blueprint("data", "data", url_prefix="/data/v1")


@data.route("/", methods=["GET"])
def get_query_results():
    try:
        print(request, 'request on get route-Query')
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
    payload = request.get_json()
    print(payload)
    query = models.Data.create(**payload)
    # print(query.___dict___, 'inside query')
    query_dict = model_to_dict(query)
    return jsonify(data=query_dict, status={"code": 201, "message": "Success"})


@data.route('/<id>', methods=["GET"])
def get_one_query(id):
    query = models.Data.get_by_id(id)
    return jsonify(data=model_to_dict(query), status={"code": 201, "message": "Success"})


@data.route('/<id>', methods=["DELETE"])
def delete_query(id):
    query = models.Data.delete().where(models.Data.id == id)
    response = query.execute()
    print(response)
    return jsonify(  # not sure why you need to jsonify
        data="resource successfully deleted",
        status={"code": 200, "message": "Resource deleted"})


@data.route('/<id>', methods=["PUT"])
def update_query(id):
    payload = request.get_json()
    print('payload:', payload)
    query = models.Data.update(**payload).where(models.Data.id == id)
    query.execute()
    updated_query = models.Data.get_by_id(id)
    return jsonify(data=model_to_dict(updated_query), status={"code": 200, "message": "Success"})

