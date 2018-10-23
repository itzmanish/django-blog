# Blog-second_project

My second project on django

# DEMO

See Demo at [maharudra.me](https://maharudra.me)

# Installation

> First rename .env.example to .env and assign important values

```
git clone https://github.com/itzmanish/blog
cd blog
pip install -r requirements.txt
pip install python-decouple
pip install django-widget-tweaks
pip install django-debug-toolbar
cd second
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
