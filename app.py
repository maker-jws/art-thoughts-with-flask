from api.data import data
from api.source import source
from api.select import select
import os
from flask import Flask, g, session, request, jsonify
from flask_login import LoginManager
from flask_cors import CORS
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route("/")  # decorator will invoke Flask
def index():  # creates
    message = "hello human = 01001000 01101001 00100000 01001000 01110101 01101101 01100001 01101110 0001010"
    return message


@app.route("/db/stat",)
def get_table_len():
    try:
        print(request, "request on get stats-Query")
        query_data = models.Data.select().count()
        query_source = models.Source.select().count()*10
        query_select = models.Select.select().count()
        print(query_data, query_source, query_select)
        current_count = {"0": query_data,
                         "1": query_source,
                         "2": query_select, }
        print(current_count)
        return jsonify(data=current_count, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "There was an error getting the resource"})


# @data.route("/", methods=["GET"])
# def get_query_results():
#     try:
#         print(request, "request on get route-Query")
#         queries = [model_to_dict(query) for query in models.Data.select()]
#         return jsonify(data=queries, status={"code": 200, "message": "Success"})
#     except models.DoesNotExist:
#         return jsonify(
#             data={},
#             status={"code": 401,
#                     "message": "There was an error getting the resource"},
#         )
CORS(app, origins=["http://localhost:3000", "http://art-thoughts-with-rock.herokuapp.com",
                   "https://art-thoughts-with-rock.herokuapp.com"], supports_credentials=True)
CORS(select, origins=["http://localhost:3000", "http://art-thoughts-with-rock.herokuapp.com",
                      "https://art-thoughts-with-rock.herokuapp.com"], supports_credentials=True)
CORS(data, origins=["http://localhost:3000",  "http://art-thoughts-with-rock.herokuapp.com",
                    "https://art-thoughts-with-rock.herokuapp.com"], supports_credentials=True)
CORS(source, origins=["http://localhost:3000", "http://art-thoughts-with-rock.herokuapp.com",
                      "https://art-thoughts-with-rock.herokuapp.com"], supports_credentials=True)
app.register_blueprint(data)
app.register_blueprint(source)
app.register_blueprint(select)

if 'ON_HEROKU' in os.environ:
    print('hitting heroku')
    models.initialize()

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
