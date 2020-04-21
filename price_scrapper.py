import requests

from preciosmaximos.repositories import ProductRepository
from preciosmaximos.transformations import ProductTransformation


class PMRetrievePrices:

    BASE_URL = "https://preciosmaximos.argentina.gob.ar/api/products"

    PROVINCE = (
        'CABA',
        'Buenos Aires',
        'Catamarca',
        'Chaco',
        'Chubut',
        'Córdoba',
        'Corrientes',
        'Entre Ríos',
        'Formosa',
        'Jujuy',
        'La Pampa',
        'La Rioja',
        'Mendoza',
        'Misiones',
        'Neuquén',
        'Río Negro',
        'Salta',
        'San Juan',
        'San Luis',
        'Santa Cruz',
        'Santa Fe',
        'Santiago del Estero',
        'Tierra del Fuego',
        'Tucumán'
    )

    def __init__(self, product_repository: ProductRepository, product_transformation: ProductTransformation):
        self._product_repository = product_repository
        self._product_transformation = product_transformation

    def run(self):
        for province in self.PROVINCE:
            print(f"Buscando los productos de la provincia {province}")
            response = requests.get(f"{self.BASE_URL}?Provincia={province}")
            json = response.json()
            json_products = json.get('result')
            print(f"Productos recuperados ({len(json_products)}). Guardando...")
            product_count = 0
            for json_product in json_products:
                product = self._product_transformation.transform(json_product)
                self._product_repository.create_or_update(product)
                product_count += 1
            print(f"Productos guardados {product_count}. Provincia {province} OK!")
        print("Terminado. Bye!")


if __name__ == '__main__':
    retrieve_service = PMRetrievePrices(ProductRepository(), ProductTransformation())
    retrieve_service.run()
