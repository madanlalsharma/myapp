from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        dbname='postgres', user='postgres',
        password='mysecretpassword', host='crunchy-db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM mytable")
    rows = cur.fetchall()
    return str(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
