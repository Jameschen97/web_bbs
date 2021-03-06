from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.topic import Topic
from models.board import Board

import uuid

csrf_tokens = dict()

main = Blueprint('topic', __name__)


@main.route("/")
def index():
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        # ms = Topic.all()
        # ms = Topic.all_delay()
        ms = Topic.cache_all()
    else:
        ms = Topic.find_all(board_id=board_id)
        # ms = Topic.cache_find(board_id=board_id)
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens[token] = u.id
    bs = Board.all()
    return render_template("topic/index.html", ms=ms, token=token, bs=bs)


@main.route('/<int:id>')
def detail(id):
    t = Topic.get(id)
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=t)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    t = Topic.new(form, user_id=u.id)
    return redirect(url_for('.detail', id=t.id))


@main.route("/delete")
def delete():
    tid = int(request.args.get('id'))
    token = request.args.get('token')
    u = current_user()
    # 判断 token 是否是我们给的
    print(csrf_tokens[token])
    if token in csrf_tokens and csrf_tokens[token] == u.id:
        csrf_tokens.pop(token)
        if u is not None:
            print('删除 topic 用户是', u, tid)
            Topic.delete(tid)
            return redirect(url_for('.index'))
        else:
            abort(404)
    else:
        abort(403)


@main.route("/new")
def new():
    bs = Board.all()
    return render_template("topic/new.html", bs=bs)
