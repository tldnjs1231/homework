# 127.0.0.1:5000
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('hw4.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():
   name_receive = request.form['name_give']
   product_receive = request.form['product_give']
   address1_receive = request.form['address1_give']
   address2_receive = request.form['address2_give']
   phone_receive = request.form['phone_give']

   # DB에 삽입할 order 만들기
   order = {
      'name': name_receive,
      'product': product_receive,
      'address1': address1_receive,
      'address2': address2_receive,
      'phone': phone_receive
      }
   # order_list에 order 저장하기
   db.orders_list.insert_one(order)
   # 성공 여부 & 성공 메시지 반환
   return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다'})


@app.route('/orders', methods=['GET'])
def read_orders():
   orders = list(db.orders_list.find({},{'_id': 0}))
   return jsonify({'result':'success', 'orders_list': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)