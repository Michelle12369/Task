# Task
Implement a Restful task list

## Setup
- Install python 3.7
- Run following commands
```
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r pip-requirements.txt
export FLASK_APP=main.py
export FLASK_ENV=development
```


## Run in container
- Run db
```
docker compose -p whoscall_task_db -f docker-compose-db.yml up
```
- After db is started, run service
```
docker compose -p whoscall_task up
```
- Test api through http://127.0.0.1:80/task


## Run service in local environment
- Prerequisite: prepare mysql db
    - Can also use the same db which you run in the previous container section. If using previous container, you can run the following command directly. 
    - If using db which is set up by yourself, you can change connection settings in app/config/config.py DevelopmentConfig.
- Run service
```
python -m flask run
```
- Test api through http://localhost:5000


## Run test in local environment
```
python -m flask test
```