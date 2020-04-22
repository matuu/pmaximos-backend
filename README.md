# pmaximos-backend
Captura de productos del programa "Precios Maximos" y exposición mediante api rest

Para utilizar este repositorio, deberá tener instalado docker y docker-compose.
Una vez clonado, ingresar al repositorio, y copiar el archivo `.env.dist` a `.env`:

```bash
cp .env.dist .env
``` 

y establacer los datos de autenticación para la db mongo.

Luego, ejecutar

```bash
docker-compose up --build
```

Eso construirá y/o bajará las imagenes docker y levantará los contenedores de modo de poder ejecutar el pryecto.
Los siguientes comandos deben ejecutarse con los contenedores en ejecución.
 

## Recuperar productos desde la API de preciosmaximos

```bash
docker-compose run web python price_scrapper.py
```

## Volcado y restauración de la base de datos mongo

Para volcar la db a un archivo, usar:

```bash
docker exec -it db_mongo mongodump -u ${MONGO_INITDB_ROOT_USERNAME} -p ${MONGO_INITDB_ROOT_PASSWORD} --out=/dumps/last/
```

Para restaurar la db desde un archivo, hacer:

```bash
docker exec -it db_mongo mongorestore -u ${MONGO_INITDB_ROOT_USERNAME} -p ${MONGO_INITDB_ROOT_PASSWORD} dumps/last/preciosmaximos/*.bson
```