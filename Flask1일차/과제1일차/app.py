from flask import Flask, render_template

app = Flask(__name__, template_folder='C:\\Users\\unign\\Desktop\\ALL\\공부\\Oz_codingSchoolwindow\\Flask1일차\\과제\\tempales')

@app.route('/')
def index():
    data = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
    return render_template('index.html', data=data)


if __name__ == "main":
    app.run(debug=True)

#users = [
#    {"username": "traveler", "name": "Alex"},
    #{"username": "photographer", "name": "Sam"},
    #{"username": "gourmet", "name": "Chris"}
#]


#과제인데
#코드 작성 이렇게 하고 html도 작성하고 flask run했는데 데이터가 제대로 안 넘어와서요 어떤 게 문제일까요?
