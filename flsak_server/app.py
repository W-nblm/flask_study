# -*- coding:utf-8 -*-
# 1.导入flask拓展
from flask import Flask, request, flash
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
import pymysql
import config
from mode import *

pymysql.install_as_MySQLdb()
# 2.创建flask应用程序实力
# 需要传输 __name__,作用是为了确定资源所在的路径
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)
app.config["SECRET_KEY"] = "123456"
# # 配置数据库的地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_sql?charset=utf8'
# # 跟踪数据库的修改  不建议开启
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
print("sdf=" + app.config["SQLALCHEMY_DATABASE_URI"])

"""
使用WTF实现表单
自定义表单类
"""


class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码不一致')])
    submit = SubmitField('提交')


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # 判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3.判断两次密码填写是否相同
        if login_form.validate_on_submit():
            print(username, password)
            return 'suss'
        else:
            flash('参数有误')
    return render_template('index_html.html', form=login_form)


# 3.定义路由及试图函数
# 默认只支持get
@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return 'Hello World!'
    # return render_template('index_html.html')


#
# db.init_app(app)
# # 删除表
db.drop_all(app=app)
#
# # 创建表
db.create_all(app=app)

# 4.启动程序
if __name__ == '__main__':
    app.run()
