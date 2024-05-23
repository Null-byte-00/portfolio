git pull
python manage.py collectstatic --noinput
python manage.py migrate
export SECRET_KEY=$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 50)
