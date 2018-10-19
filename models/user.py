# from models import Model
from models.mongo import Mongo


# class User(Model):
#     """
#     User 是一个保存用户数据的 model
#     """
#
#     def __init__(self, form):
#         self.id = form.get('id', None)
#         self.username = form.get('username', '')
#         self.password = form.get('password', '')
#         self.user_img = 'default.jpg'
#
#     @staticmethod
#     def salted_password(password, salt='$!@><?>HUI&DWQa`'):
#         import hashlib
#
#         def sha256(ascii_str):
#             return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
#
#         hash1 = sha256(password)
#         hash2 = sha256(hash1 + salt)
#         return hash2
#
#     @staticmethod
#     def hashed_password(pwd):
#         import hashlib
#         # 用 ascii 编码转换成 bytes 对象
#         p = pwd.encode('ascii')
#         s = hashlib.sha256(p)
#         # 返回摘要字符串
#         return s.hexdigest()
#
#     @classmethod
#     def register(cls, form):
#         name = form.get('username', '')
#         pwd = form.get('password', '')
#         if len(name) > 2 and User.find_by(username=name) is None:
#             u = User.new(form)
#             u.password = u.salted_password(pwd)
#             u.save()
#             return u
#         else:
#             return None
#
#     @classmethod
#     def validate_login(cls, form):
#         u = User(form)
#         user = User.find_by(username=u.username)
#         if user is not None and user.password == u.salted_password(u.password):
#             return user
#         else:
#             return None


class User(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('username', str, ''),
        ('password', str, ''),
        ('user_img', str, ''),
    ]

    def __init__(self):
        self.user_img = 'default.jpg'

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        import hashlib

        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    @staticmethod
    def hashed_password(pwd):
        import hashlib
        # 用 ascii 编码转换成 bytes 对象
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        if len(name) > 2 and User.find_by(username=name) is None:
            u = User.new(form)
            u.password = u.salted_password(pwd)
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        u = User()
        u.username = form.get("username", '')
        u.password = form.get("password", "")
        user = User.find_by(username=u.username)
        if user is not None and user.password == u.salted_password(u.password):
            return user
        else:
            return None
