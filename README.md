# Airport API Service

The Airport API Service is a versatile backend solution for
managing airport-related data and facilitating flight bookings.
It offers CRUD (Create, Read, Update, Delete) operations for cities,
routes, airplanes, and flights for administrators while providing the
opportunity for everyone to book seats for flights through orders.

## Installation

Clone this repository:
```
git clone https://github.com/Gvilion/airport-api-service.git
```

## Environment Setup

1. Rename the provided `env.sample` file to `.env` in the project directory.
2. Open the `.env` file and replace `SECRET_KEY` with your actual
secret key.

## Dockerization and Running

1. Make sure you have Docker and Docker Compose installed on your system. 
You can download and install them from the official 
[Docker website](https://www.docker.com/products/docker-desktop).
2. Build and run the Docker containers using docker-compose by running 
the following command in the project directory:

```
docker-compose up --build
```

## Accessing the Application

You can now access the API by opening your web browser 
and navigating to http://localhost:8000.

## Endpoints

```
"crew": "http://localhost:8000/api/airport/crew/",
"airplane-type": "http://localhost:8000/api/airport/airplane-type/",
"airplane": "http://localhost:8000/api/airport/airplane/",
"airport": "http://localhost:8000/api/airport/airport/",
"route": "http://localhost:8000/api/airport/route/",
"flight": "http://localhost:8000/api/airport/flight/",
"order": "http://localhost:8000/api/airport/order/"
"documentatoin": "http://127.0.0.1:8000/api/schema/"
                 "http://127.0.0.1:8000/api/schema/swagger-ui/"
                 "http://127.0.0.1:8000/api/schema/redoc/ "
```

## Schema

![schema.png](./pictures_for_readme/schema.png)

## Screenshots

![airport.png](./pictures_for_readme/airport.png)
![unauthenticated.png](./pictures_for_readme/unauthenticated.png)
![swagger.png](./pictures_for_readme/swagger.png)


