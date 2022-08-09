# API YaMDb via Docker #
****
#### Description ####
API YaMDb collects score and reviews on different titles in different categories and genres. Categories and genres are customizable. Also there is an option to add comments to reviews. In this project API YaMDb starts via Docker

#### Technology Stack ####
Python 3.7 / Django 2.2.16 / Django REST framework 3.12.4 / Docker 20.10.17 / PostgeSQL 13.0

#### How to start API YaMDb locally via Docker ####
```
git clone https://github.com/Immalakhovskii/infra_sp2.git    # clone repository
cd infra_sp2/infra    # change directory to infra/
docker-compose up -d --build    # create and activate Docker containers
docker-compose exec web python manage.py createsuperuser    # create superuser
```
Now admin zone of the project available at http://localhost/admin/, API requests also can be performed (see full list of requests in ReDoc documentation)
- Note that to perform docker comands **Docker must be installed and running** on your computer (https://www.docker.com/products/docker-desktop/)
- Examples of enviromental variables can be seen at infra/.env.example

To deactivate and delete containers perform:
```
docker-compose down -v
```

#### API YaMDb Documentation ####
Accessible at http://localhost/redoc/ while containers are active. To receive **token** make POST request with "email" and "username" to http://localhost/api/v1/auth/signup/, after receiving confirmation code make POST request with "confirmation_code" and "username" to http://localhost/api/v1/auth/token/