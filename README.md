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

# run proyect with uvicorn
```
poetry run start
```


Thanks to
https://github.com/Progyan1997/fastapi-clean-example