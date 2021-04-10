STEPS TO RUN PROJECT

install virtualenv if not installed: sudo pip3 install virtualenv
create virtual environment: virtualenv .env
activate virtual env by: source .env/bin/activate
install all requirements by: pip3 install -r requirements.txt

cd task
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver