# web_bbs
## requires:
- MongoDB
- pymongo
- redis
- Flask
## description
- 使用 **MongoDB** 作为数据库服务器, **pymongo** 作驱动 
- 编写 **ORM** 模型, 存取数据
- 使用 **redis** 对常用数据进行缓存, 使存取数据更快
- 基于 **Flask** 搭建服务器, 用 **Blueprint** 作动态路由
- 服务器使用 **Gunicorn (WSGI)** , **Nginx** 进行反向代理
- 实现了*用户功能, 板块功能, 发布功能, 评论功能, 私信功能*等论坛的基本功能
