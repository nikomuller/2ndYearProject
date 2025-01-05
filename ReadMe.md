#How To Run

git clone https://github.com/nikomuller/Shoe-eCommerce-Website.git

cd your-repository-folder

python -m venv pyvenv 
pyvenv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations 
python manage.py migrate

python manage.py runserver


EzKickz E-commerce website
2nd Year Project - 2023

External Packages :
    asgiref==3.5.2
    certifi==2022.12.7
    charset-normalizer==2.1.1
    crispy-bootstrap5==0.7
    distlib==0.3.6
    Django==4.1.4
    django-crispy-forms==1.14.0
    filelock==3.8.2
    idna==3.4
    Pillow==9.3.0
    platformdirs==2.6.0
    requests==2.28.1
    sqlparse==0.4.3
    stripe==5.0.0
    tzdata==2022.7
    urllib3==1.26.13
    virtualenv==20.17.1

