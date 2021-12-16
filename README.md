# README.md

# Description

`wooper-stats` is a platform designed to quickly get Twitch.tv analytics projects off the ground and into an analysis and dashboarding environment.  

Installing and running the scripts will result in the following by default:
- A postgres database in a docker container
- A pgadmin4 instance running in docker container
- A FastAPI implementation that allows for easy functionality expansion or CRUD operations out of the box
- An ETL script that uses `requests` library to get the top currently live streams from Twitch.tv





# Prerequisites

1. Docker
2. Docker-compose
3. Twitch API access/authentication 
4. Python



---
### 1. Docker

If you don't have Docker Desktop (Mac, Windows) or Docker Engine (Hi Linux friends), you can follow the instructions linked [here](https://docs.docker.com/get-docker/).  

Docker is really good at making restarting and sharing database environments a very short string. But what is really convenient is when you combine the docker platform with docker compose to manage multiple processes and link them together seamlessly.

You may need to configure permissions so that you don't have to type `sudo` every time you try to interact with docker in the terminal if this is your first time installing docker.

### 2. Docker-Compose

[Install here](https://docs.docker.com/compose/install/).  
Docker compose lets us turn on and off our postgres database and pgadmin instances with a flip of the switch.  
If something goes wrong in the database when testing and want to throw it away, it's a matter of turning off the containers, deleting them and spinning up again. The other handy feature is that the containers bulit by the `docker-compose.yml` can address each other by service name any time an address or connection is required.

### 3. Twitch API Access  
Follow these instructions to gain access to the API: https://dev.twitch.tv/docs/api/  
The app name is going to be whatever you call what you build on top of this repo. Don't worry about installing the twitch CLI, you only need the credentials to put in your .env file

### 4. Python

This is a python project. Use whatever venv manager you like. I use conda. 


# Installation

1. Make sure you have all of your prerequisites
2. Clone the repo
3. Use your preferred environment manager to install from the `requirements.txt`
4. Create a `.env` file with the following contents at the root of this repo, and make sure ".env" is in your `.gitignore` 

```
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="password"
POSTGRES_DB="postgres"
POSTGRES_HOST="localhost"

PGADMIN_DEFAULT_EMAIL="admin@admin.com"
PGADMIN_DEFAULT_PASSWORD="root"

TWITCH_CLIENT_ID="your_credentials_here"
TWITCH_CLIENT_SECRET="your_secret_here"
```

Both the docker-compose file and the ETL script will read in the secrets from environment variables rather than having them public and hardcoded. If you intend to push your container to Docker Hub or create a remote deployment through a cloud platform, I suggest migrating to Docker Swarm/Secrets for managing these. 

5. Make sure that the docker service is running and open on your computer.
6. Use docker-compose to build the containers, and start them

## How to use docker-compose  

- In terminal, `cd` to root of this repo
- Run `docker-compose up -d` to start up the containers in detached mode. If you get an error regarding no default env vars, make sure your CWD is root of the repo. 

- This will create a postgres instance without any tables initialized and a pgadmin instance.
- You can then use the pgadmin container to interface graphically with the database. 
- Use `docker-compose down` to shut down the instances
- Use `docker-compose ps` to see if any are running

If you want to interface with the database directly, in terminal use `docker-compose exec database bash` to gain access to the postgres container's terminal.
Then use `psql -U postgres` to enter database. `\dt` will list tables found. 


## Initializing the postgres tables and populating database

1. Navigate to the root of the repo and run the following commands:

```
python src/services.py
python src/twitch_etl_pipe.py
```

The first command will build a table in the postgres container according to the schema described by the SQLAlchemy mappings. 

The second command will use the `requests` library to get the top 100 channels currently live on twitch and populate the table in the database that you just created. 


## Starting and accessing FastAPI
1. If you are in the root dir of this repo, `cd` into the `src/` subfolder. From there, run the following command: 

```
uvicorn main:app --reload
```

This will start the app in the terminal, and you can inspect the endpoints and try interacting with the data by navigating to `localhost:8000/docs` in your browser   

This is what you should see:
![alt text](https://github.com/tyleretheridge/wooper-stats/blob/main/assets/images/fastapidocs.png?raw=true)

## Using pgadmin4
1. In a browser, go to `localhost:5050` and login to the dashboard using the PGADMIN credentials listed in the `.env` sample above. 
2. In the left pane, right-click the Servers then select `Create > Server...`

3. In the pop-up window use whatever name you want for the Name field in the General tab. 

4. Navigate to the Connection tab. In the first field, `Host name/address`, put "database". This is made possible because docker-compose links the database and pgadmin instances, and you can reference them by the service names in the `docker-compose.yml` file. 

5. For username and password, enter the username and password credentials **for the database**. If you left them as the defaults in the sample .env, then they will be "postgres" and "password" respectively. 

6. Click Save in the bottom right and the connection should populate in the left pane for you to explore. 

# Random Notes
To improve the automated nature of this project, create a python image definition in a Dockerfile and use that image in the `docker-compose.yml` as new service. Doing so will allow the `services.py` and `uvicorn` commands to be bound and run automatically when all of the containers are started simultaneously.   


The current `requests` implementation is engineered to focus on ETL operations and building a system that strictly enforces uniform and standardized data models in the warehousing. Rerunning the etl script without flushing the database will likely cause errors with duplicate primary keys if a streamer is still live when you recall the script. To avoid this, alter the data query and table structure so that the data being scraped isn't at risk of this error. Use `sudo rm -rf pgdata/` at the root of this repo to delete the database (not the container). This is useful when stuff goes really wrong or you need to change the database structure.


There is a `sql/` folder that contains the a SQL query that will generate the same table as the `service.py` does in the postgres container if you want to directly interface with raw SQL. To implement, add the following line to the `docker-compose.yml` file under volumes for the database service.   
```
- ./sql/database_init.sql:/docker-entrypoint-initdb.d/database_init.sql
```
This project simply aims to abstract towards more rigid modeling in management of the database systems, and has migrated from this implementation. Another method is to use Alembic. 