from bson.json_util import dumps

from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful.utils import cors

from preciosmaximos.repositories import ProductRepository


app = Flask(__name__)
api = Api(app)


class Products(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        page = int(request.args.get('page', 1))
        size = int(request.args.get('size', 50))
        skip = (page - 1) * size
        product_repository = ProductRepository()
        _products = product_repository.list_all().skip(skip).limit(size)
        return dumps(_products)


api.add_resource(Products, '/products')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
