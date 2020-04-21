from preciosmaximos.models import Product


class ProductTransformation:
    """
    Transform product json from https://preciosmaximos.argentina.gob.ar API to Product models.
    """
    def transform(self, product_json) -> Product:
        return Product(
            id_product=product_json["id_producto"],
            suggested_price=product_json["Precio sugerido"],
            product_name=product_json["Producto"],
            brand=product_json["marca"],
            province=product_json["Provincia"],
            region=product_json["Region"],
            category=product_json["categoria"],
            subcategory=product_json["subcategoria"],
            product_name_safe=product_json["Producto_s_tilde"]
        )
