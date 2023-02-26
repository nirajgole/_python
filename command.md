1. Create folder fast-react with sub-folders named frontend and backend
2. inside frontend run ```npx create-react-app .```
3. inside backend run ```virtualenv venv```
4. to activate backend virtual env run ```venv/scripts/activate```
5. backend-> install ```pip install fastapi sqlalchemy pymysql PyMySQL[rsa] uvicorn```
6. on command line windows cmd ```docker run --name mysqldb -e MYSQL_DATABASE=test -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:latest```
7. frontend to start the react application ```npm run start```
8. backend to start fastapi application ```uvicorn index:app --reload```
9. add requirements.txt to backend ```pip freeze > requirements.txt```