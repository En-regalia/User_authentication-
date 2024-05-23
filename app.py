from flask import Flask, render_template
import _mysql_connector
import mysql


app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('index.html')

if __name__ == '__main__':
    app.run(debug=True)

mybd = _mysql_connector.connect(
    host = 'localhost'
    user = 'yourusername'
    password = 'your_password'
)

