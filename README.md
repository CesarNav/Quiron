# quiron

Run the app in local environment:

- Install virtual env `pip install virtualenv`
- Initialize virtual environment `virtualenv .env`
- Install requirements `pip install -r requirements.txt`
- Install [Postgres](https://www.postgresql.org/) database engine, create a new database and update connection string on `Quiron/Quiron/settings.py`
- Run database migrations with `python Quiron/manage.py migrate`, this will create the schema on the database.
- Run the application by executing `python Quiron/manage.py runserver`.
