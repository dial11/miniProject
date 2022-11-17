from pymongo import MongoClient
client = MongoClient('mongodb+srv://jun:doyc93%40%40%21%40@cluster0.i1qtcm3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.p2

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/p2')
def home():
   return render_template('p2.html')

@app.route("/p2_comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
   
    doc = {
        'comment': comment_receive,
        
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'입력 완료!'})

@app.route("/p2_comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id': False}))

    return jsonify({'comment':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

