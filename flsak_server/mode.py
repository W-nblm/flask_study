from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
两张表
角色（管理员/普通用户 )
用户
"""


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 在一的一方，写关联
    # users = db.relationship('User'): 表示和User模型发生了关联，增加了一个user属性
    # backref='role':表示role是User要用的属性
    users = db.relationship('User', backref='role')

    # repr()方法表示一个刻度字符串
    def __repr__(self):
        return 'Role: %s %s' % (self.name, self.id)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # User 希望有role属性，但是这个属性的定义，需要在另一个模型中定义

    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name, self.id, self.email, self.password)
