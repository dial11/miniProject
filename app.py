from pymongo import MongoClient
client = MongoClient('mongodb+srv://jun:doyc93%40%40%21%40@cluster0.i1qtcm3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.p2

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/individual/p2')
def p2home():
   return render_template('p2.html')

@app.route("/p2_comment", methods=["POST"])
def p2comment_post():
    comment_receive = request.form['comment_give']

    comment_list = list(db.p2_comment.find({}, {'_id': False}));
    count = len(comment_list) + 1

    doca = {
        'comment': comment_receive,
        'num': count
    }
    db.p2_comment.insert_one(doca)
    return jsonify({'msg':'입력 완료!'})

@app.route("/p2_comment", methods=["GET"])
def p2comment_get():
    comment_list = list(db.p2_comment.find({}, {'_id': False}))
    return jsonify({'comment':comment_list})

@app.route('/p2_delComment', methods=['POST'])
def p2_comment_delete():
    num_receive = request.form['num_give']

    db.p2_comment.delete_one({'num': int(num_receive)});

    return jsonify({'result': 'success', 'msg': '삭제 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

