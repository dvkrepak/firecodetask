<img align="right" src="https://notion-emojis.s3-us-west-2.amazonaws.com/v0/svg-twitter/1f40d.svg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="200" height="400" />

## **Technical task in Python for FireCode**

Made by **Denis Krepak**

## **Project Description**

### **English Brief** - [FireCode Junior Python Task](https://www.notion.so/Django-Junior-Techical-Task-Eng-8162ac222824461ebd13aac3f9a02356)

### **Russian Brief -** [FireCode Junior Python Task](https://www.notion.so/Django-Junior-Techical-Task-Rus-fd26c321e5b54e27a53013f49ac02822)


Wrote on **Python** using **Django**, **Django Rest Framework**. **PostgreSQL** is used as a **DBMS**.


## **Deployment on a local machine**
1. Connect to PostgreSQL:
```
psql -U postgres
```
Create DB with nane "fctaskdb":
```
CREATE DATABASE fctaskdb;
```
Connect to new DB:
```
\c fctaskdb;
```
2. Clone the repository:
```
git clone https://github.com/dvkrepak/firecodetask.git
```
3. Create virtual environment with name "venv":
```
python3 -m venv venv
```
Activating venv:
```
source venv/bin/activate
```
4. Go to the folder with app:
```
cd firecodetask/
```
5. Installing all packages from requirements.txt:
```
pip install -r requirements.txt
```
6. Make migrations:
```
python manage.py migrate
```
7. Create superuser:
```
python manage.py createsuperuser
```
8. Launch project:
```
python manage.py runserver
```
9. Fill the DB(optional):
```
python manage.py loaddata shop/fixtures/citydata.json
python manage.py loaddata shop/fixtures/streetdata.json
python manage.py loaddata shop/fixtures/storedata.json
```

Project will be available at **http://127.0.0.1:8000/**

## **Views**
#### **localhost/city/** - all cities from the db
#### **localhost/city_slug/street** - all street in a current city
#### **localhost/shop/** - create new store
#### **localhost/shop/?street=&city&open=** - all stores with filters 
 