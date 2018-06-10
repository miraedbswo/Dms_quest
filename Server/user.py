from models import *
from flask import request, Response, jsonify


@app.route('/sign_up', methods=['POST'])
def insert():
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']

    row = User(user_id=user_id, user_pw=user_pw)
    db.session.add(row)
    db.session.commit()

    return Response('회원가입이 완료되었습니다.', 201)


@app.route('/user/select/<id>', methods=['GET'])
def select(id):
    row = User.query.filter_by(user_id=id).first()

    return jsonify({
        'id': row.user_id,
        'pw': row.user_pw,
        'signup_time': row.signup_time,

        'stay_status': row.stay,

        'goingout_status': row.goingout
    })


@app.route('/user/delete', methods=['DELETE'])
def delete():
    user_id = request.form['user_id']

    row = User.query.filter_by(user_id=user_id).first()
    db.session.delete(row)
    db.session.commit()

    return Response('탈퇴 성공', 200)


@app.route('/user/new_pw', methods=['POST'])
def update():
    user_id = request.form['user_id']
    new_pw = request.form['new_pw']

    row = User.query.filter_by(user_id=user_id).first()
    row.user_pw = new_pw
    db.session.commit()

    return Response('비밀번호가 재설정되었습니다.', 201)
