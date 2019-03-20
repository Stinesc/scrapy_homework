# Scrapy homework
## How to run
```bash
In first terminal:

git clone https://github.com/Stinesc/scrapy_homework.git
python3 -m venv ./venv
. venv/bin/activate
pip3 install -r requirements.txt
cd ./lordandtaylor
scrapy crawl jeans

In second terminal:

cd ../lordandtaylor_site
celery -A lordandtaylor_site worker --loglevel=info

In third terminal:

python3 manage.py migrate
python3 manage.py runserver
```
