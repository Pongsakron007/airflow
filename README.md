# airflow
Airflow project for more comprehension.

## First step
After clone this repository follow this step below.

## For the very first time you run the project use this command.
docker-compose up --build
docker-compose up -d --build

## If you want to stop 
docker-compose stop (if you run with docker-compose up -d command)
ctrl +c and then docker-compose stop (if you run with docker-compose up command)

## If you want to delete 
docker-compose down

## How to get username and password 
first time username is "admin" and "password" adrees in log after we run container for the first time(Pls note that password will apear only first time when you start container otherwise you must delete container and volumn then get start again)