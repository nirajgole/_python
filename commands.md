1. Install Virtual Environment
>`py -m pip install virtualenv`
2. Create a virtual environment:
>`py -m virtualenv env`
3. Activate virtual environment
>`env\Scripts\Activate`
4. install Django
>`pip install django`
5. Create a new Django project
>`django-admin startproject mysite`
6. Run local server
>`python .\mysite\manage.py runserver`
7. Start New App under MySite
>`python .\mysite\manage.py startapp polls`
8. Create/ Make changes to db according application
>`python .\mysite\manage.py migrate`
9. Make Database changes based on models
>`python .\mysite\manage.py makemigrations polls`
10. To apply database changes run 8th command
11. To use django api/shell
>`python .\mysite\manage.py shell`
12. Create super-user for database admin functionality
>`python \mysite\manage.py createsuperuser`