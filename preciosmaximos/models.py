from dataclasses import dataclass

from bson import ObjectId


@dataclass
class Product:
    id_product: int
    suggested_price: float
    product_name: str
    brand: str
    province: str
    region: str
    category: str
    subcategory: str
    product_name_safe: str = ''
    _id = ObjectId = None

    def to_dict(self):
        return self.__dict__