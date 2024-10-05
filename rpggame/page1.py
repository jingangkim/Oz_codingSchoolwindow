from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/page1', methods=['POST'])
def page1():
    # request.form에서 전달된 데이터를 처리
    data = request.form['your_data']  # intro.html에서 전달된 데이터 가져오기
    # 여기서 원하는 코드 실행
    result = some_function(data)  # 예시: some_function은 사용자가 정의한 함수
    return render_template('page1.html', result=result)