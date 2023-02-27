from flask import Flask,render_template,jsonify
app = Flask(__name__)

Jobs = [{
  'id':1,
  'title':'Date Analyst',
  'location':'Delhi',
  'salary':100000
},
{
  'id':2,
  'title':'Date Scientist',
  'location':'Noida',
  'salary':120000 
},
{
  'id':3,
  'title':'Software Enginner',
  'location':'Mumbai',
  'salary':150000
}]

@app.route("/")
def hello_world():
  return render_template ('home.html',jobs=Jobs)



@app.route("/jobs")
def jobs():
  return jsonify(Jobs)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True) 