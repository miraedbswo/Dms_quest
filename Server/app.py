from user import *


@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']
    row = User.query.filter_by(user_id=user_id, user_pw=user_pw).first()

    if row is not None:
        return Response('로그인 성공', 200)
    else:
        return Response('로그인 실패', 401)


@app.route('/apply/residual/<id>/<status>', methods=['Get'])
def residual(id, status):
    """
    1 : 금요귀가
    2 : 토요귀가
    3 : 토요귀사
    4 : 잔류
    """
    Database = User.query.filter_by(user_id=id).first()

    if Database is None:
        return 'incorrect id'

    Database.stay = status

    db.session.commit()
    return Response('잔류 신청에 성공했습니다', 200)


@app.route('/apply/go_out/<id>/<status>', methods=['GET'])
def go_out(id, status):
    """
    1 : 토요일 외출
    2 : 일요일 외출
    3 : 토, 일요일 외출
    """
    Database = User.query.filter_by(user_id=id).first()

    if Database is None:
        return 'incorrect id'

    Database.goingout = status

    db.session.commit()
    return Response('외출 신청에 성공했습니다.', 200)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
