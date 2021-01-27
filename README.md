# Olympics API

An API based on the [120 years of Olympic history: athletes and results Dataset](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results) powered by Django REST Framework

## Instalation

Create a virtual enviroment, clone this repository and install dependecies (on linux):
```bash
python3 -m venv olympics-api
source olympics-api/bin/activate
git clone https://github.com/joelschutz/olympics-api.git
pip install requeriments.txt
```

Initialize the database and create superuser. Make sure to edit the database preferencies in the settings.py file if you don't intend to use it woth sqlite:
```bash
cd olympics-api
python manage.py migrate
python manage.py createsuperuser # You will be prompt to define a username and password
python manage.py drf_create_token your-username # This keep this token secret
```

Import the dataset information to the database, use the files provided by the dataset above:
```bash
python manage.py import_noc dataset/noc_regions.csv
python manage.py import_events dataset/athlete_events.csv #This may take a while
```

Once all the data is in the up you can start the server and test it:
```bash
python manage.py runserver
curl http://127.0.0.1:8000/events?athlete_NOC=105&sport=2 # This will retrieve all the Judo events where a Japanese athlete competed
```
## Usage

This API implements all the basic http methods to interact with the database(GET, PUT, DELETE, POST and PATCH). Althought, to be able to change any data o must be autheticated. It is recommended to use the token generated earlier in the request headers, as the example:
```bash
curl -H 'Authorization: Token your-auth-token' http://127.0.0.1:8000/sports
```
You can also request an token using the */api-token-auth* endpoint:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"your-username", "password":"your-password"}' http://127.0.0.1:8000/api-token-auth/
```
Session and Http authentication are also valid.

## Endpoints

Each endpoint will provide give access to an especific part of the data structure of the dataset with different filter options. The main one is the */events*, which is able to provide the complete information of the event and related data structures.

You can create new instances of a datastucture using the POST method. This example will create a new medal with the name "Foo":
```bash
curl -X POST -H "Content-Type: application/json" -H 'Authorization: Token your-token' -d '{"name":"Foo"}' http://127.0.0.1:8000/medals/
```
To interact with a particular instance in the database o must include its id after the endpoint. This example will delete the previously created medal:
```bash
curl -X DELETE -H "Content-Type: application/json" -H 'Authorization: Token your-token' http://127.0.0.1:8000/medals/5/
```

The allowed method are:
| Method | Behavior                             | Scope            |
|--------|--------------------------------------|------------------|
| POST   | Creates an new instance              | List only        |
| GET    | Retrieves an instance or list        | List or Instance |
| PUT    | Updates an instance's data           | Instance only    |
| DELETE | Delete an instance                   | Instance only    |
| PATCH  | Partially updates an instance's data | Instance only    |

### List
---
In all endpoints, if no instance is specified when called, it will return an unfiltered list with all its contents with 100 results per page by default. The received data is structured as follows:
| Key      | Value                                               |
|----------|-----------------------------------------------------|
| count    | The total number of instances retrieved by the call |
| next     | URL for the next page in of results                 |
| previous | URL for the previous page in of results             |
| results  | List of instance retrieved                          |

The following parameters are allowed in all the endpoints:
| Parameter | Behavior                                                             |
|-----------|----------------------------------------------------------------------|
| limit     | Number of results per page                                           |
| offset    | Number of results to offset the page(used to navegate between pages) |

In addition to these, each endpoint has its own filters. See below for more info.

### */events*
---
This endpoint is responsable for the Events in the database. Events are singular participations of an athlete in an Olympic competition. The received data is structured as follows:

| Key          | Value                                                                                       |
|--------------|---------------------------------------------------------------------------------------------|
| id           | The id of the specific instance                                                             |
| athlete      | The related Athlete instance related to this event. See /athletes for more info.            |
| athlete_age  | The Athlete age at the time of the event.                                                   |
| athlete_team | The Team that the Atlhete represented in de event. It is related to the NOC but not always. |
| athlete_NOC  | The related NOC instance related to this event. See /nocs for more info.                    |
| game         | The related Game instance related to this event. See /games for more info.                  |
| competition  | The related Competition instance related to this event. See /competitions for more info.    |
| medal        | The related Medal instance related to this event. See /medals for more info.                |

You can use this keys as parameters for filtering the results. In addition, the parameters below are also valid:
| Parameter    | Type | Notes          |
|--------------|------|----------------|
| sport        | int  | Instance id    |
| year         | int  |                |
| season       | str  | Case sensitive |
| medal        | int  | Instance id    |

### */nocs*
---
This endpoint is responsable for the NOCs(National Olympic Committees) in the database. NOCs are the organizations responsable for promoting the Olympic Games in a country. The received data is structured as follows:

| Key    | Value                                             |
|--------|---------------------------------------------------|
| id     | The id of the specific instance                   |
| noc    | Unique 3 letter combination that identifies a NOC |
| region | Official name of the region or country            |
| notes  | May contain alternative region names              |

You can use this keys as parameters for filtering the results.

### */sports*
---
This endpoint is responsable for the Sports in the database. The received data is structured as follows:

| Key  | Value                           |
|------|---------------------------------|
| id   | The id of the specific instance |
| name | Official name of the Sport      |

You can use this keys as parameters for filtering the results.

### */games*
---
This endpoint is responsable for the Games in the database. Games are specific editions of the Olympic Games. The received data is structured as follows:

| Key    | Value                           |
|--------|---------------------------------|
| id     | The id of the specific instance |
| year   | Year when the edition occured   |
| season | Season of the edition           |
| city   | Host city of the Games          |

You can use this keys as parameters for filtering the results.

### */athletes*
---
This endpoint is responsable for the Athletes in the database. The received data is structured as follows:

| Key    | Value                           |
|--------|---------------------------------|
| id     | The id of the specific instance |
| name   | Name of the athlete             |
| sex    | Gender of the athlete           |
| height | Height of the athlete           |
| weight | Weight of the athlete           |

You can use this keys as parameters for filtering the results.

### */competitions*
---
This endpoint is responsable for the Competitions in the database. Competitions specific modalities of a particular Sport. The received data is structured as follows:

| Key    | Value                                                                              |
|--------|------------------------------------------------------------------------------------|
| id     | The id of the specific instance                                                    |
| name   | Name of the competition                                                            |
| sport  | The related Sport instance related to this competition. See /sports for more info. |

You can use this keys as parameters for filtering the results.

### */medals*
---
This endpoint is responsable for the medal types in the database. The received data is structured as follows:

| Key    | Value                                                                              |
|--------|------------------------------------------------------------------------------------|
| id     | The id of the specific instance                                                    |
| name   | Name of medal or 'NA' if no medal was gifted                                       |

## Demo

A live demo is live at [olympics-api-jss.herokuapp.com](https://olympics-api-jss.herokuapp.com/). Contact me at [contato@joelschutz.com.br](mailto:contato@joelschutz.com.br) for credentials if you need it.

## License

Distributed under the MIT License. See LICENSE for more information.

This license only applies to the code in this repository. Contact the the creators about the dataset license.
