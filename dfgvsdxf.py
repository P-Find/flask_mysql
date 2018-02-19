from flask import Flask, g
import pymysql
app = Flask(__name__)


@app.before_request
def before_request():
    g.conn = pymysql.connect(host='localhost',
                             user='root',
                             passwd='mysql',
                             db='testdata',
                             charset='utf8')

    g.cur = g.conn.cursor(pymysql.cursors.DictCursor)


@app.teardown_request
def close_mysql(exception=None):
    g.conn.close()


@app.route('/')
def index():
    try:
        g.cur.execute("select * FROM data")
    except Exception as e:
        print(e)

    print(g.cur.fetchall())
    return "aaa"


if __name__ == '__main__':
    app.run()