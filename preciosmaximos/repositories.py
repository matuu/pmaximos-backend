from typing import Tuple

from pymongo.cursor import Cursor

from preciosmaximos.db_connection import db
from preciosmaximos.models import Product


class ProductRepository:
    def __init__(self):
        self._products = db.products

    def create_or_update(self, product: Product) -> Tuple[bool, Product]:
        result = self._products.update_one(
            filter=dict(id_product=product.id_product, province=product.province),
            update={"$set": product.to_dict()},
            upsert=True)
        product._id = result.upserted_id
        created = not result.raw_result['updatedExisting']
        return created, product

    def list_all(self) -> Cursor:
        return self._products.find()