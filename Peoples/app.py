"""
С помощью библиотеки faker необходимо создать три файла:
1) humans.txt -> ФИО (hint -> .name(), разделитель запятая)
2) names.txt  -> Имена (hint -> .first_name())
3) users.txt  -> ФИО (hint -> .simple_profile(), разделитель точка с запятая)
"""

from flask import Flask, render_template
from faker import Faker


app = Flask(__name__)
fake = Faker("ru_RU")





@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)