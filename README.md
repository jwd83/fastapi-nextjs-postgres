# FastAPI + Next.js + Postgres

## Boilerplate / Tutorial

My own notes following along with the tutorial at:

[https://www.travisluong.com/how-to-build-a-full-stack-next-js-fastapi-postgresql-boilerplate-tutorial/](https://www.travisluong.com/how-to-build-a-full-stack-next-js-fastapi-postgresql-boilerplate-tutorial/)

## Get Postgres

We're going to need a local postgres server so let's get that handled first.

[https://postgres.app/](https://postgres.app/)

Install a local macos postgres server using postgres.app. Be sure to follow the
install docs to set PATHs on their website. Startup the postgres app and get
your initial setup done and running.

# Python FastAPI backend

The following section takes place in the fnp-backend folder.

Inside the fnp-backend folder create and activate the python virtual
environment.

    $ python -m venv venv
    $ . venv/bin/activate

Install FastAPI, and other dependencies. Note that psycopg2 will fail to install
if postgres.app has not been installed with the PATHs set correctly.

    $ pip install fastapi "uvicorn[standard]" gunicorn psycopg2 sqlalchemy alembic "databases[postgresql]" python-dotenv

Once the install completes successfully we can do our first pip freeze to get a
requirements.txt file.

    $ pip freeze > requirements.txt

Once postgres is running we can try...

    createdb nfp_boilerplate_dev
    createuser nfp_boilerplate_user -P

...to create the database and user. The password for the user will be prompted.
I set the password to `test` while following the tutorial.

Next we will enable the database migrations using alembic. See the alembic
documentation in travis notes for more information.
