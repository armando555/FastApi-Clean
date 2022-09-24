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