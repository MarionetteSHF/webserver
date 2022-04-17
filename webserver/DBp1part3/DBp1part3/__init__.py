from flask import Flask,render_template
from .views.category import ind
from .views.login import auth
from DBp1part3.views.test2 import testblue2
from . import sql
from .views import post



def create_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key='hanfushi'

    @app.route('/index')
    def index():
        db = sql.get_db()
        cur = db.cursor()
        cur.execute(
            'SELECT i.item_id, i.title, i.price, i.neededitem, p.image_source '
            'FROM Items_Posted i LEFT JOIN '
            '(SELECT DISTINCT ON (item_id) item_id, image_source FROM Photos ORDER BY item_id, image_source DESC, item_id) p '
            'ON i.item_id = p.item_id '
            'ORDER BY i.posted_at DESC',)
        rows = cur.fetchall()
        return render_template('webpage/index.html', rows=rows)


    app.register_blueprint(auth)
    app.register_blueprint(testblue2)
    app.register_blueprint(post.bp)
    app.register_blueprint(ind)
    app.add_url_rule('/', endpoint='index')
    # app.register_blueprint(testblue, url_prefix ='/web')
    # app.register_blueprint(testblue2, url_prefix ='/admin')
    return app