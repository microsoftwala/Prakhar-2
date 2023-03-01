from sqlalchemy import create_engine, text

db_con="mysql+pymysql://34adkx5cxuz5izr49wms:pscale_pw_JKYb1ivzj8kMxxNyP8whBaDBKbBJpwb9HPslekRU695@aws.connect.psdb.cloud/bhai?charset=utf8mb4"
# db_con = os.environ['DB_CONNECTION']
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

def load_job_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    my_dict = []
    for row in result.all():
      my_dict.append(row)
  
    return my_dict

def add_application_to_db(job_id,data):
  with engine.connect() as connection:
    # query = text("INSERT INTO application (job_id,full_name,email,linkedin_url,education_url,work_experiance,resume_url) VALUES (%d,%s,%s,%s,%s,%s,%s)")

    # connection.execute(query,job_id,
    #              data['fullname'],
    #              data['email'],
    #              data['emailss'],
    #              data['education'],
    #              data['experiance'],
    #              data['emails'])

    t = text("SELECT * FROM jobs WHERE id =:user_id")
    result = connection.execute(t, user_id=2)
    return result