from sqlalchemy import create_engine, text
import os
# print(sqlalchemy.__version__)
db_con = "mysql+pymysql://34adkx5cxuz5izr49wms:pscale_pw_JKYb1ivzj8kMxxNyP8whBaDBKbBJpwb9HPslekRU695@aws.connect.psdb.cloud/bhai?charset=utf8mb4"
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
