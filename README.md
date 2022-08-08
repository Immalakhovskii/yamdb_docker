# API YaMDb via Docker #
****
#### Description ####
API YaMDb collects score and reviews on different titles in different categories and genres. Categories and genres are customizable. Also there is an option to add comments to reviews. In this project API YaMDb starts via Docker

#### Technology Stack ####
Python 3.7 / Django 2.2.16 / Django REST framework 3.12.4 / Docker 20.10.17 

#### How to start API YaMDb locally via Docker ####
```
git clone https://github.com/Immalakhovskii/infra_sp2.git    # clone repository
cd infra_sp2/infra    # change directory to infra/
docker-compose up -d --build    # start composing Docker containers
docker-compose exec web python manage.py migrate    # make migrations
docker-compose exec web python manage.py createsuperuser    # create superuser
docker-compose exec web python manage.py collectstatic --no-input    # collect static
```
Now admin zone of the project available at http://localhost/admin/, API requests also can be performed (see full list in ReDoc documentation). 
- Note that to perform docker comands **Docker must be installed and running** on your computer (https://www.docker.com/products/docker-desktop/). 
- Examples of enviromental variables can be seen in infra/.env.example

To deactivate and delete containers perform:
```
docker-compose down -v
```

#### Full Yatube_API Documentation ####
Accessible at http://localhost/redoc/ while containers are active