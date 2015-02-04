Install instructions
===========================

git clone git@github.com:Sashkow/FortyTwoTestTask2.git

cd FortyTwoTestTask2

virtualenv --no-site-packages .env

source .env/bin/activate

.env/bin/pip install -r requirements.txt

python manage.py syncdb --noinput

python manage.py migrate
