from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
from user_routes import create_user_blueprint

app = Flask(__name__)

app.config['mysql_host'] = 'localhost'
app.config['mysql_user'] = 'root'
app.config['mysql_PASSWORD'] = '@Ab1480718'
app.config['mysql_DB'] = 'jingang'

mysql = MySQL(app)

#blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

user_blp = create_user_blueprint(mysql)
api.register_blueprint(user_blp)


from flask import render_template
@app.route('/users_interface') #테스팅할 주소
def users_interface():
    return render_template("users.html")



