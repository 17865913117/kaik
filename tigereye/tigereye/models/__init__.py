from flask import json as _json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Model(object):

    @classmethod
    def get(cls, primary_key):
        return cls.query.get(primary_key)

    def put(self):
        db.session.add(self)


    @classmethod
    def commit(cls):
        # 提交至数据库执行
        db.session.commit()

    @classmethod

    def rollback(cls):
        # 回滚
        db.session.rollback()

    def save(self):
        try:
            self.put()
            self.commit()
        except Exception:
            self.rollback()
            raise
    def delete(self):
        db.session.delete(self)

    # 重写json方法，将传入的数据直接转化为json对象
    def __json__(self):
        _d = {}
        for k, v in vars(self).items():
            # 以-开头的建对应的一个对象而不是值
            if k.startswith("_"):
                continue
            _d[k] = v
        return _d


class JsonEncoder(_json.JSONEncoder):
    # 重载flask的jsonEncoder类

    def default(self, o):
        # 重载default方法以支持Model类对象json序列化
        if isinstance(o, Model):
            # 返回重写的json方法
            return o.__json__()
        # 返回系统中的json方法
        return _json.JSONEncoder.default(self, o)
