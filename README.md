# Auth API
This is a Auth API that provides a set of endpoints to perform various operations. This README file provides instructions on how to install and run the Auth API on your local machine.

## Installation
To install and run the Auth API, you need to have Python3 installed on your machine.

Clone the repository using the following command:


```sh
git clone https://github.com/Sagg-301/4di_sergio_garcia_test.git
```

Navigate to the project directory using the following command:

```sh
cd 4di_sergio_garcia_test
```

Create a virtual environment using the following command:

```sh
python3 -m venv venv
```

Activate the virtual environment using the following command:

```sh
source venv/bin/activate
```

Install the required dependencies using the following command:

```sh
pip install -r requirements.txt
```
### Configuration
The Flask API uses environment variables to configure various aspects of the app, such as the database URI and secret key. To set these variables, create a .env file in the root directory of the project and add the following variables:

```
DEBUG: Used to start the app in debug mode
DB_HOST: Database host
DB_NAME: Databae name
DB_USER: Database user
DB_PASSWORD: Database password
DB_PORT: Database port
SECRET_KEY: Secret key for signing cookies
ALLOWED_ORIGINS: CORS allowed origins

```

Example .env:
```
DEBUG = True
DB_HOST = localhost
DB_NAME = 4di
DB_USER = admin
DB_PASSWORD = 12345678
DB_PORT = 5432
SECRET_KEY = secret-4di
DROP_DB = False
#CORS
ALLOWED_ORIGINS = 'http://localhost:3000'
```



### Usage
To run the Auth API, follow these steps:

Activate the virtual environment using the following command:

```sh
source venv/bin/activate
```

Execute the migrations
Start the server using the following command:

```sh
flask db upgrade
```

Start the server using the following command:

```sh
flask run
```

Access the endpoints using the following URL:

```
http://localhost:5000/
```
## API Reference

#### Login

```http
  POST /login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user` | `string` | **Required**. user name |
| `password` | `string` | **Required**. password |

#### Get logged user info

```http
  GET /who-am-i
```

#### Log out

```http
  POST /logout
```
