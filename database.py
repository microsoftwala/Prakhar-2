from sqlalchemy import create_engine, text
import os
# print(sqlalchemy.__version__)
db_con = os.environ['DB_CONNECTION']
engine = create_engine(db_con,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    my_dict = []
    for row in result.all():
      my_dict.append(row)
    return my_dict
