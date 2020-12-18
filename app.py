
from flask import Flask,render_template
#from fireinit import firebase,db,dataget
import humidity
app = Flask(__name__)

@app.route('/')
def index():
  data = humidity.getTemp()
  return render_template('index.html', data=data)

@app.route('/supplylist')
def supplylist():
# userlist = dataget()
  return render_template('/supplylist.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000, debug=True)

