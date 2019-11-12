from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import choices
from flask_mysqldb import MySQL
import string

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '3306'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'url_shortener'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = SQLAlchemy(app)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''. join(choices(characters, k=5))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()

        return short_url


@app.route('/', methods=['POST', 'GET'])
def home():
    # original_url = request.form['original_url']
    # link = Link(original_url=original_url)
    # db.session.add(link)
    # db.session.commit()
    if request.method == 'POST'
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO links('original_url') VALUES(%s), (original_url) ")

        mysql.connection.commit()

        cur.close()
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return '', 404

if __name__ == "__main__":
    app.run(debug=True)