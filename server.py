import Attendance
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('model.html')

@app.route('/attendance/')
def attendance():
  execfile("Attendance.py")

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
