<h1>Penguin Protocol Backend</h1>
<p>This Python Flask server provides an interface to a SQLite Database for the Penguin Protocol Android Application</p>

<h3>API</h3>

```
POST /basic-query
payload = {
    'sel': str
    'table': str,
    'where': str,
}
headers = {
    'Content-type': 'application/json'
}
returns = {
    'rows' = list["attr1", "attr2", "attr3"]
}


POST /add-location
payload = {
    'name': str,
    'address': str,
    'city': str,
    'country': str
}
headers = {
    'Content-type': 'application/json'
}
returns = {
    'id': int,
    'success': bool
}


POST /add-user
payload = {
    'name': str,
    'sem_attend': str,
    'program': str
}
headers = {
    'Content-type': 'application/json'
}
returns = {
    'id': int,
    'success': bool
}


POST /add-review
payload = {
    'user': str,
    'date': str,
    'location': str,
    'text': str,
    'stars': int,
    'price': int
}
headers = {
    'Content-type': 'application/json'
}
returns = {
    'id': int,
    'success': bool
}


POST /add-program
payload = {
    'name': str,
    'school': str,
    'city': str,
    'country': str
}
headers = {
    'Content-type': 'application/json'
}
returns = {
    'id': int,
    'success': bool
}
```
