### Django Environment Variables
----

- ``` APPLICATION_NAME```: The name of the application.
- ``` DEBUG```: Debug mode. If on, will display details of error pages. If your app raises an exception when DEBUG is on, will display a detailed traceback, including a lot of metadata about the environment, such as all the currently defined Django settings (from base.py). Never deploy a site into production with DEBUG turned on.
- ``` DJANGO_SETTINGS_MODULE```: The Django settings module to use.
- ``` SECRET_KEY```: The secret key to use for cryptographic operations should be set to a unique, unpredictable value. Never deploy a site into production with the default secret key.
- ``` DATABASE_URL```: The URL of the database to use. You can choose from a variety of database engines.
- ``` ALLOWED_HOSTS```: The comma seperated hostnames that Django will use to access the site.
- ``` TIME_ZONE```: The timezone to use for the site.
- ``` ENABLE_LOGGING```: If on, will enable exception logging in rotated file handler.
- ``` ENABLE_AUTO_LOGGING```: If on, will enable auto exception logging in rotated file handler.
- ``` LOGGING_DIR```: The directory to use for exception logging.
- ``` ENABLE_DEBUG_TOOLBAR```: If on, will enable debug toolbar.


### Run Docker Compose To Run The Application
----

- ``` docker-compose --project-name=ecommerce -f docker-compose.yml up ``` - Run the project environment.
- ``` docker-compose --project-name=ecommerce -f docker-compose.yml up --build -d ``` - Build the project environment and run it.
- ``` docker-compose --project-name=ecommerce -f docker-compose.yml -f docker-compose.production.yml up``` - Run the production environment.
- ``` docker-compose --project-name=ecommerce -f docker-compose.yml -f docker-compose.production.yml up --build -d ``` - Build the production environment and run it.

### Other Common Docker Commands
----

- ``` docker-compose --project-name=ecommerce down ``` - Stop all containers.
- ``` docker-compose --project-name=ecommerce -f docker-compose.yml down ``` - Stop all containers in the compose file.
- ``` docker-compose --project-name=ecommerce down --remove-orphans ``` - Stop all containers and delete orphaned containers associated with them.
- ``` docker network create supernet ``` - Create network 'supernet' if it doesn't exists.
- ``` docker system prune -af ``` - Remove all stopped containers, networks, volumes, and images.
- ``` sudo docker network create supernet ``` - Create the network manually.
- ``` sudo docker-compose --project-name=ecommerce -f docker-compose.yml up --build -d ``` - Run the project environment.
- ``` sudo docker logs -f --tail 100 ecommerce_1 ``` - Display django consol logs.
- ``` sudo docker exec -it ecommerce_1 sh ``` - Access django shell.

### Backup & Restore Database
----

- ``` docker exec -t PostgreSQL pg_dumpall -c -U ecommerceUser > dump/dump_latest.sql ```  - Backup
- ``` cat dump/dump_latest.sql | docker exec -i PostgreSQL psql -U ecommerceUser ``` - Restore

