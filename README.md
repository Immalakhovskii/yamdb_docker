# YaMDb (Docker Edition) #

### Description ###
Web API service YaMDb collects scores and reviews on different works of art (titles) in different categories (e.g. films, music, books) and genres (e.g. drama, comedy, ballad). Anonymous can read descriptions of titles, reviews and comments. Authenticated user can publish own reviews to titles, give a score to titles, comment own reviews and other users. Titles, categories and genres can be created and updated by Admin. While the project activated see full detailed API documentation here: http://localhost/redoc/

### Technology Stack ###
Python 3.7 / Django 2.2.16 / Django REST framework 3.12.4 / Docker 20.10.17 / PostgreSQL 13.0

### How to start YaMDb via Docker ###
```
# clone repository and change directory to infra/
git clone https://github.com/Immalakhovskii/infra_sp2.git
cd infra_sp2/infra

# copy .env.example with valid data as .env
cp .env.example .env

# create and activate Docker containers
docker-compose up -d --build

# create new superuser in case you want to
docker-compose exec web python manage.py createsuperuser    
```
Now admin site of the project available at http://localhost/admin/. API requests can be performed by addresses starting with http://localhost/api/v1/ (see full list of available requests here: http://localhost/redoc/). Database already has 10 genres, 4 titles, 4 categories and superuser Admin
```
# accesses admin zone as Admin:
Username: Admin
Password: youllneverguess
``` 
- Note that to perform docker comands **Docker must be installed and running** on your computer (https://www.docker.com/products/docker-desktop/)
- Actual enviromental variables for the YaMDb stored at infra/.env.example. Safety precautions ignored for the public availability of the project

To deactivate and delete containers and static volumes perform:
```
docker-compose down -v
```

### Get JWT token ###
- To receive **token** make POST request with "email" and "username" to http://localhost/api/v1/auth/signup/. After receiving confirmation code make POST request with "confirmation_code" and "username" to http://localhost/api/v1/auth/token/. Token must be passed with **"Bearer"** header
