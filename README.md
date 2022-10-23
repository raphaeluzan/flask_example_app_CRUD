## Flask APP

Application developed with python & flask for learning purposes

- [x] Flask init app
- [x] Flask Get endpoint (serveur side)
- [x] Flask Get endpoint (client side)
- [x] Flask CRUD endpoint (serveur side)
- [x] Flask CRUD endpoint (client side)
- [x] UI with flask and template
- [ ] Interact with the sqlite application
- [x] Use docker-compose to launch and create the dockerized application


## How to run it locally

```
git clone https://github.com/raphaeluzan/flask_example_app_CRUD.git
cd example-flask-crud/
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=crudapp.py
flask db init
flask db migrate -m "entries table"
flask db upgrade
export FLASK_ENV=development
flask run
```


## Flask Get endpoint (client side)


### CURL way

```
$ curl -XGET http://localhost:5000/
{"reponse": "{1: {'title': 'azeaze', 'content': 'azeaze'}, 2: {'title': 'azeaze', 'content': 'azeaze'}, 3: {'title': 'azeaze', 'content': 'azeazea'}, 4: {'title': 'aa', 'content': ' zzz ze'}, 5: {'title': 'aze', 'content': 'aze'}, 6: {'title': 'a', 'content': 'a'}, 7: {'title': 'a', 'content': 'a'}}"}
```

### Python way

```
import requests

res = requests.get("http://localhost:5000/")
print(res.text)

>>> {"reponse": "{1: {'title': 'azeaze', 'content': 'azeaze'}, 2: {'title': 'azeaze', 'content': 'azeaze'}, 3: {'title': 'azeaze', 'content': 'azeazea'}, 4: {'title': 'aa', 'content': ' zzz ze'}, 5: {'title': 'aze', 'content': 'aze'}, 6: {'title': 'a', 'content': 'a'}, 7: {'title': 'a', 'content': 'a'}}"}
```



## Flask CRUD endpoint (serveur side)
```
$ curl -XPOST http://localhost:5000/add -d "title=a&description=atetetetettete"
```
## use docker-compose to launch and create the dockerized 

* open docker 
* build the image
`docker-compose build`

* launch the image
`docker-compose up`

* open the application in browser
`http://localhost:8000/index`

