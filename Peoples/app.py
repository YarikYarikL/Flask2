"""
С помощью библиотеки faker необходимо создать три файла:
1) humans.txt -> ФИО (hint -> .name(), разделитель запятая)
2) names.txt  -> Имена (hint -> .first_name())
3) users.txt  -> ФИО (hint -> .simple_profile(), разделитель точка с запятая)
"""

import sys
from flask import Flask, abort, render_template
from faker import Faker


app = Flask(__name__)
fake = Faker("ru_RU")


def create_files():
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


@app.route("/names")
def get_names():
    names = list()
    with open("files/names.txt", encoding="utf-8") as f:
        for raw_line in f:
            names.append(raw_line.strip())
    return render_template("names.html", people_names=names) #{"people_name": names}


@app.route("/table")
def get_usertable():
    entities = list()
    with open("./files/humans.txt", encoding="utf-8") as f:
        for raw_line in f:
            data = raw_line.strip().split(',')
            keys = ['last_name', 'name', 'surname']
            person = dict(zip(keys, data))
            entities.append(person)
    return render_template('table.html', names_list=entities)


@app.route("/users")
def get_usersinfo():
    humans = []
    with open('./files/users.txt', encoding='utf-8') as file:
        for row in file:
            raw_data = row.strip().split(';')
            keys = ['login', 'full_name', 'sex', 'address', 'email', 'birthday']
            user = {}
            for i in range(len(raw_data)):
                user[keys[i]] = raw_data[i]
            humans.append(user)
    return render_template('users_list.html', users_data=humans)


@app.route("/users/<login>")
def get_singleuserinfo(login):
    user_data = None
    with open('./files/users.txt', encoding='utf-8') as file:
        for row in file:
            raw_data = row.strip().split(';')
            if raw_data[0] == login:
                keys = ['login', 'full_name', 'sex', 'address', 'email', 'birthday']
                user_data = {}
                for i in range(len(raw_data)):
                    user_data[keys[i]] = raw_data[i]
                return render_template('user_info.html', user_data=user_data)
    if user_data is None:
        abort(404)





if __name__ == '__main__':
    #передаем из командной строки в виде: python app.py --files
    #if len(sys.argv) >1 and sys.argv[1] == "--files":
    #    create_files()
    app.run(debug=True)