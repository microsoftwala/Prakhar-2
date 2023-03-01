from flask import Flask, render_template,request
from database import load_jobs_from_db, load_job_from_db,add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  Jobs = load_jobs_from_db()
  return render_template('home.html', jobs=Jobs)




@app.route("/job/<id>")
def jobs_data(id):
  Jobs = load_job_from_db()
  return render_template('jobpage.html', jobs=Jobs,id=int(id))



@app.route("/job/<id>/apply",methods=['post','get'])
def apply_for_job(id):
  data = request.form
  Jobs = load_job_from_db()
  add_application_to_db(int(id),data)
  return render_template('application_submitted.html',application=data,jobs=Jobs)


              
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
