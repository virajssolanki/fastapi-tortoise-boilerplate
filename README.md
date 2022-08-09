## about this boilerplate

This is my humble try to build best scalable fastapi and tortoise project structure. 

- tortoise is used as orm.
- aerich is used for migrations.
- database is in postgressql. 
- python 3.10 is used.


## run boilerplate

1. Take a clone
```
git clone https://github.com/virajssolanki/fastapi-tortoise-boilerplate.git
```

2. Install required packages (virtual environment recommended)
```
pip install -r requirements.txt
```

3. rename env.example to .env and also change DATABASE_URL to your db url

4. Generate migrations and 
```
aerich init -t app.main.aerich_config
```

5. Initialize the database
```
aerich init-db
```

6. run server
```
uvicorn app.main:app --reload
```


## extra info

- use following to run server at certain port
```
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload --debug
```

following commands will be used to migrate if make any changes in models

- Generate migrations:
```
aerich migrate
```

- Migrate changes:
```
aerich upgrade
```


Booom, happy coding