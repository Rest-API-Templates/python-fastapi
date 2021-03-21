## Local Setup
```console
foo@bar:~$ pip3 install -r requirements.txt --user
foo@bar:~$ uvicorn app:app --host 0.0.0.0
```

## Docker Setup
```console
foo@bar:~$ docker build . -t fastapi-rest
foo@bar:~$ docker run  -p 8000:8000 fastapi-rest
```

## Documentation Url
see documentation [here](http://127.0.0.1:8000/docs)
