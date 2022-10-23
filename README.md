## Flask APP

Application developed with python & flask for learning purposes

- [ ] Flask init app
- [x] Flask Get endpoint (serveur side)
- [ ] Flask Get endpoint (client side)
- [x] Flask CRUD endpoint (serveur side)
- [ ] Flask CRUD endpoint (client side)
- [x]UI with flask and template
- [ ] Jupiter
- [ ] Saturn
- [ ] Uranus
- [ ] Neptune
- [ ] Comet Haley

## How to run 


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
flask run
```