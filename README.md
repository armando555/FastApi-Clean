#FAST API CLEAN ARCHITECTURE

# This is a very important thing
The modules of services and repositories are not using because they are for specific things. In this case we are using https://github.com/awtkns/fastapi-crudrouter to build the pydantic schemas and the routers automatically. But if you want to build the manually use this https://github.com/Progyan1997/fastapi-clean-example repo to follow the strategy. Please note that in this repo, he is using SQLAlchemy but I'm using Tortoise.


# setup the .env file with all the configuration according to the deployment

# stop database container
```bash
docker stop mysql-db && docker rm mysql-db
```
# run a database container 
```
docker run -d -p 33061:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=root mysql
```
# create database
```
docker exec -i -t mysql-db bash

mysql -u root -p

create database test_bookstore;
```


# install dependencies
```
poetry install
```

# NOTE
Don't forget select the python interpreter 

## in visual studio code
CTRL+P


Write symbol greater ">"


Choose the option Python: Select Interpreter 


finally, select the interpreter with the tag Poetry

# run proyect with uvicorn
```
poetry run start
```


Thanks to
https://github.com/Progyan1997/fastapi-clean-example