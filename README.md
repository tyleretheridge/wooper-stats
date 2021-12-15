finish api
build custom python image container
create dockerfile for that image and postgresql database
add creds to .env
use env vars in docker compose

## How to use docker-compose  

- In terminal, cd to root of this repo
- Create a .env file with the following credentials:
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
- Run `docker-compose up -d` to start up the containers in detached mode. If you get an error regarding no default env vars, make sure your CWD is root of the repo. 
- This will create a postgres database following the schema described in `sql/database_init.sql`
- You can then use the pgadmin container to interface graphically with the database. 

If you want to interface with the database directly, in terminal use `docker-compose exec database bash` to gain access to the postgres container's terminal.

Then use `psql -U postgres` to enter database. `\dt` will list tables found. 