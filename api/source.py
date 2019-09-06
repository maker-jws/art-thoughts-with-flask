from flask import Blueprint
import models
from flask import request
from flask import jsonify
from playhouse.shortcuts import model_to_dict

source = Blueprint("source", "source", url_prefix="/source/v1")


@source.route("/", methods=["GET"])
def get_all_url_results():
    try:
        print(request, 'request on get route-sourceUrl')
        sources = [model_to_dict(source) for source in models.Source.select()]
        return jsonify(data=sources, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={},
            status={"code": 401,
                    "message": "There was an error getting the resource"},
        )


@source.route('/', methods=["POST"])
def store_source_url():
    print(request, "request")
    payload = request.get_json()
    print(payload)
    source = models.Source.create(**payload)
    # print(query.___dict___, 'inside query')
    source_dict = model_to_dict(source)
    return jsonify(data=source_dict, status={"code": 201, "message": "Success"})


@source.route('/<id>', methods=["GET"])
def get_one_source(id):
    source = models.Source.get_by_id(id)
    return jsonify(data=model_to_dict(source), status={"code": 201, "message": "Success"})


@source.route('/<id>', methods=["DELETE"])
def delete_source(id):
    query = models.Data.delete().where(models.Data.id == id)
    response = query.execute()
    print(response)
    return jsonify(  # not sure why you need to jsonify
        data="resource successfully deleted",
        status={"code": 200, "message": "Resource deleted"})


@source.route('/<id>', methods=["PUT"])
def update_source(id):
    payload = request.get_json()
    print('payload:', payload)
    source = models.Source.update(**payload).where(models.Source.id == id)
    source.execute()
    updated_source = models.Source.get_by_id(id)
    return jsonify(data=model_to_dict(updated_source), status={"code": 200, "message": "Success"})
