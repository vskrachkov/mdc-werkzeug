Using PostgreSQL with Python
============================

For starting postgres docker container execute:

    docker run --name pgsql \
        -e POSTGRES_PASSWORD=BiGveryStrongPassword \
        -e POSTGRES_USER=mdc \
        -e POSTGRES_DB=mdc_database \
        -v /Users/vs/Documents/Draft/PostgresSQL/examples/sql:/docker-entrypoint-initdb.d \
        -v /Users/vs/Documents/Draft/PostgresSQL/src/mdc/db:/database_scripts/mdc \
        -v /Users/vs/Documents/Draft/PostgresSQL/examples/tutorial:/database_scripts/tutorial \
        -p 5432:5432 \
        -d postgres


Connection via psycopg2:

    conn = p.connect(dbname='mdc_database', 
                     user='mdc', 
                     password='BiGveryStrongPassword', 
                     host='localhost')
                     
Connection via psql from docker container:

    psql "dbname=mdc_database user=mdc password=BiGveryStrongPassword 
    host=localhost"
