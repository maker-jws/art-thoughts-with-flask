from flask import Blueprint
import models
from flask import request
from flask import jsonify
from playhouse.shortcuts import model_to_dict

select = Blueprint("select", "select", url_prefix="/select/v1")


@select.route("/", methods=["GET"])
def get_all_select_results():
    try:
        print(request, 'request on get route-selectUrl')
        select = [model_to_dict(select) for select in models.Select.select()]
        return jsonify(data=select, status={"code": 200, "message": "Success"})

    except models.DoesNotExist:
        return jsonify(
            data={},
            status={"code": 401,
                    "message": "There was an error getting the Selection"},
        )


@select.route('/', methods=["POST"])
def store_select_url():
    print(request, "request")
    payload = request.get_json()
    print(payload, "after json payload")
    select = models.Select.create(**payload)
    select_dict = model_to_dict(select)
    return jsonify(data=select_dict, status={"code": 201, "message": "Success"})


@select.route('/<id>', methods=["GET"])
def get_one_select(id):
    select = models.Select.get_by_id(id)
    return jsonify(data=model_to_dict(select), status={"code": 201, "message": "Success"})


@select.route('/<id>', methods=["DELETE"])
def delete_select(id):
    select = models.Select.delete().where(models.Select.id == id)
    response = select.execute()
    print(response)
    return jsonify(  # not sure why you need to jsonify
        data="selection successfully deleted",
        status={"code": 200, "message": "Selection deleted"})


@select.route('/<id>', methods=["PUT"])
def update_select(id):
    payload = request.get_json()
    print('payload:', payload)
    select = models.Select.update(**payload).where(models.Select.id == id)
    select.execute()
    updated_select = models.Select.get_by_id(id)
    return jsonify(data=model_to_dict(updated_select), status={"code": 200, "message": "Success"})
