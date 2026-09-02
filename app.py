from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks_database.db"
# initialize the app with the extension
db = SQLAlchemy(app)


# Creating a Model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer())
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Task {self.id}"
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)