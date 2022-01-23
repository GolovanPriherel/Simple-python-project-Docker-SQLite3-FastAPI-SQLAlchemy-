# Simple-python-project-Docker-SQLite3-FastAPI-SQLAlchemy-
Simple python project with: Docker SQLite3 FastAPI SQLAlchemy 

# О проекте
Простой проект на питоне с докером, SQLite3, FastAPI и SQLAlchemy <br>
Реализован простой CRUD.

# Установка
Для установки достаточно склонировать проект, и запустить докер-композ:<br>
<code>docker-compose up --build</code>

# Как использовать
Обращаться к локальному хосту на порте (по умолчанию) :5001<br>
<code> http://localhost:5001/<эндпоинт>/ </code>
<br>Например: http://localhost:5001/show/ - покажет всю информацию в таблицах БД
 
# Эндпоинты
- / - root (корневой эндпоинт, ничего не делает)
- /create/ - создаёт таблицы
- /show/ - выводит всю информацию из таблицы
- /insert/ - заполняет таблицы информацией (по пути: /src/Database_Utils/DB_Requests/ в методе **insert_tables** класса **DatabaseORM** вводится фиксированная информация, меняйте её, если нужно изменить ввод)
- /delete/ - удаляет все данные в таблицах
