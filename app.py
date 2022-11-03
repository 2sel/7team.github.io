from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.3ytzhsg.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/templates", methods=["POST"])
def templates_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.templates.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }
    db.templates.insert_one(doc)

    return jsonify({'msg': '소중한 의견 감사합니다!'})

@app.route("/templates/done", methods=["POST"])
def templates_done():
    num_receive = request.form['num_give']
    db.templates.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '삭제했습니다:)'})


@app.route("/templates", methods=["GET"])
def templates_get():
    comment_list = list(db.templates.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
