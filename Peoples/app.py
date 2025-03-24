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


def create_files() -> None:
    with open("./files/humans.txt", 'w', encoding="utf-8") as humans_f:
        for _ in range(10):
            print(*fake.name().split(), sep=',', file=humans_f)


    with open("./files/names.txt", 'w', encoding="utf-8") as names_f:
        for _ in range(10):
            print(fake.first_name(), sep=',', file=names_f)


    with open("./files/users.txt", 'w', encoding="utf-8") as users_f:
        for _ in range(10):
            print(*fake.simple_profile().values(), sep=';', file=users_f)



@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    create_files()
    app.run(debug=True)