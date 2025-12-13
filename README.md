# dataset_api
A FastAPI-based API exposing structured dataset from a SQL database.

This project uses a movie database as an example use case, but the goal is generic:
**expose structured data through a clean, documented HTTP API**, deployed as a real system service.

---

## Context
The MySQL database contains a single table of movies, with basic metadata :
<img width="550" height="330" alt="image" src="https://github.com/user-attachments/assets/47a284a3-c383-4a08-a166-7a25c880e1e1" />

The aim of this project is to expose these data accross two endpoints :
* getFilms()
<img width="256" height="186" alt="image" src="https://github.com/user-attachments/assets/98659cfe-4b52-40cf-8a63-ea0864526c97" />

* getFilmData(id)
<img width="597" height="152" alt="image" src="https://github.com/user-attachments/assets/24d01529-62b9-404b-9971-703dea47890b" />

Endpoints are accessible only if the request contains a valid API key :

<img width="291" height="52" alt="image" src="https://github.com/user-attachments/assets/92b4d7be-9216-4d04-aabb-088369eebd02" />

---

## App description
* `main.py` - entry point
* `endpoints.py` - HTTP endpoints (FastAPI)
* `database.py` - MySQL database access
* `security.py` - Api KEY verification
* `config.ini` - runtime configuration

---

## How to run it
If you want to deploy and use the app, you will need a MySQL database with a table named 'film' with atleast the 2 following properties :
- film_id (integer, unique)
- film_name (string)
Additional columns are optional and will be automatically exposed by the API.

To deploy the app, clone the repository using git clone command, then setup a virtual environnement with the following ones :
```
python3 -m venv env
source env/bin/activate # if needed
pip install --upgrade pip
pip install -r requirements.txt
```

When it's done, you have to setup the config.ini file :
- Remove the .empty in the name of the file
- Fill the file with your own database credentials

Finally, you can test your API with the following :
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
You can now call your API, try with http://0.0.0.0:8000/ping in your browser, it should return {"status" : "ok"}.
If you want to call the other endpoints, do not forget to put as a header for your request the API KEY.

You can use a browser extension like Header Editor for the purpose if needed :
<img width="633" height="33" alt="image" src="https://github.com/user-attachments/assets/7864cd1b-f7f1-4f4c-a367-ba1c62403fb3" />

You should now have everything to know to use the app on a local computer.
If you want to learn how to deploy it on ubuntu server, do not hesitate to contact me directly (check GitMews on github).
