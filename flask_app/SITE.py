import sqlite3

from flask import Flask, url_for, request, redirect

app = Flask(__name__)
logins = []
login_password = []
con = sqlite3.connect('LOGIN.db')
cur = con.cursor()
result = cur.execute("""SELECT Login FROM SITE""").fetchall()
for elem in result:
    logins.append(*elem)
con.commit()
message = ''
buffer = []
dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
dic1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
er = ['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
error_1 = False
last_page = ""


@app.route('/', methods=['POST', 'GET'])
def title_page():
    global message
    message = ''
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <link rel="shortcut icon" href="static/img/favicon.ico" type="image/x-icon">
                            <meta charset="utf-8">

                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha428-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Титульная страница</title>
                          </head>
                          <body>
                            <h1>
                                <div class="alert alert-primary" role="alert" align="center">Добро пожаловать!</div>
                            </h1>
                            <form class="login_form" method="post">
                                <button float="right" type="submit" class="btn btn-primary" name="name" value="log">Войти</button>
                                <button tfloat="right" ype="submit" class="btn btn-primary" name="name" value="reg">Регистрация</button>
                            </form>
                            <div class="all">
                            <input checked type="radio" name="respond" id="desktop">
                                <article id="slider">
                                        <input checked type="radio" name="slider" id="switch1">
                                        <input type="radio" name="slider" id="switch2">
                                        <input type="radio" name="slider" id="switch3">
                                    <div id="slides">

                                        <div id="overflow">
                                            <div class="image">
                                                <article><img src="static/img/1.jpg"></article>
                                                <article><img src="static/img/2.jpg"></article>
                                                <article><img src="static/img/3.jpg"></article>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="controls">
                                        <label for="switch1"></label>
                                        <label for="switch2"></label>
                                        <label for="switch3"></label>
                                    </div>

                                    <div id="active">
                                        <label for="switch1"></label>
                                        <label for="switch2"></label>
                                        <label for="switch3"></label>
                                    </div>
                                </article>
                        </div>
                        </html>'''
    elif request.method == 'POST':
        check = request.form['name']
        if check == 'log':
            return redirect(url_for('login'))
        elif check == 'reg':
            return redirect(url_for('register'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    global login_password, message
    con = sqlite3.connect('LOGIN.db')
    cur = con.cursor()
    second_result = cur.execute("""SELECT Login, Password FROM SITE""").fetchall()
    for elem in second_result:
        login_password.append(elem)
    global message
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <link rel="shortcut icon" href="static/img/favicon.ico" type="image/x-icon">
                            <meta charset="utf-8">

                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha428-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>
                                ВХОД
                            </title>
                          </head>
                          <body>
                            <h1>
                                <div class="alert alert-primary" role="alert">
                                    Вход
                                </div>
                            </h1>
                            <div>
                                <form class="login_form" method="post">
                                    <textarea class="form-control" id="about" rows="1" placeholder="Введите логин" name="login"></textarea>
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <button type="submit" class="btn btn-primary">
                                        Войти    
                                    </button>
                                    <a href="{url_for("register")}">
                                        У меня нет аккаунта
                                    </a>
                                    <br>%s
                        </html>''' % message
    elif request.method == 'POST':
        message = ''
        flag = True
        for i in range(len(login_password)):
            if request.form['login'] != login_password[i][0] and request.form['password'] != login_password[i][1]:
                message = 'НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ'
                flag = False
            else:
                flag = True
                break
        if flag:
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))


text = ''
login_errors = ''


@app.route('/register', methods=['POST', 'GET'])
def register():
    global text, logins, login_errors, message
    message = ''
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">

                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha428-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>
                                РЕГИСТРАЦИЯ
                            </title>
                          </head>
                          <body>
                            <h1>
                                <div class="alert alert-primary" role="alert" color="red">
                                    Регистрация
                                </div>
                            </h1>
                            <div>
                                <form class="login_form" method="post">
                                    <textarea class="form-control" id="about" rows="1" placeholder="Введите имя"name="name"></textarea>
                                    <textarea class="form-control" id="about" rows="1" placeholder="Введите фамилию"name="surname"></textarea>
                                    <textarea class="form-control" id="about" rows="1" placeholder="Введите логин"name="login"></textarea> 
                                    <div class="controls">
                                    <small class="form-text text-muted">
                                        %s
                                    </small>

                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                        placeholder="Введите адрес почты" name="email">
                                    <small id="emailHelp" class="form-text text-muted">
                                        Мы никогда не будем распространять ваш email
                                    </small>

                                    <input type="password" class="form-control" id="password" 
                                        placeholder="Введите пароль" name="password">
                                    <input type="password" class="form-control" id="password" 
                                        placeholder="Подтвердите пароль" name="password1">
                                    <small class="form-text text-muted">
                                        %s
                                    </small>
                                    <div class="form-group">
                                        <label for="form-check">
                                            Укажите пол
                                        </label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                                value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                                value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        Записаться
                                    </button>
                                </form>
                            </div>
                          </body>
                        </html>''' % (login_errors, text)
    elif request.method == 'POST':
        if request.form['password'] == request.form['password1'] and request.form['name'] != '' \
                and request.form['surname'] != '' and request.form['login'] != '' and request.form['email'] != '' \
                and request.form['password'] != '' and request.form['sex'] != '':
            if request.form['login'] not in logins:
                values = [request.form['name'], request.form['surname'], request.form['login'], request.form['email'],
                          request.form['password'], request.form['sex']]
                con = sqlite3.connect('LOGIN.db')
                cur = con.cursor()
                cur.execute("INSERT iNTO SITE VALUES (?, ?, ?, ?, ?, ?)", values)
                con.commit()
                return redirect(url_for('login'))
            else:
                login_errors = "ЛОГИН ЗАНЯТ"
                return redirect(url_for('register'))
        elif request.form['password'] != request.form['password1']:
            text = "ПАРОЛИ НЕ СОВПАДАЮТ"
            return redirect(url_for('register'))
        else:
            text = "ЗАПОЛНИТЕ ВСЕ ПУНКТЫ"
            return redirect(url_for('register'))


answer = ''


@app.route('/main', methods=['POST', 'GET'])
def main():
    global answer, buffer, error_1, er, message
    message = ''
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.css"
                            integrity="sha428-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>
                                КОНВЕРТОР
                            </title>
                          </head>                   
                          <body>
                            <h1>
                                <div class="alert alert-primary" role="alert" color="red">
                                    Конвертор
                                </div>
                            </h1>
                            <div>
                                <form class="login_form" method="post">
                                <div class="form-group">
                                <label for="form-check">
                                    Укажите вид системы счисления для ввода
                                </label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_in" id="1" value="two_in" checked>
                                    <label class="form-check-label" for="1">
                                      Двоичная
                                    </label>     
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_in" id="2" value="eight_in">
                                    <label class="form-check-label" for="2">
                                       Восьмеричная   
                                    </label>     
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_in" id="3" value="ten_in">
                                    <label class="form-check-label" for="3">
                                    Десятичная 
                                    </label>     
                                </div>                           
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_in" id="4" value="sixteen_in">
                                    <label class="form-check-label" for="4">
                                     Шестнадцатеричная
                                    </label>
                                </div>
                                <label for="input">
                                    Ввод
                                </label>
                                <input name="input" type="input" class="form-control" id="input">
                                <label for="form-check">
                                    Укажите вид системы счисления для вывода
                                </label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_out" id="5" value="two_out" checked>
                                    <label class="form-check-label" for="5">
                                      Двоичная
                                    </label>     
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_out" id="6" value="eight_out">
                                    <label class="form-check-label" for="6">
                                       Восьмеричная   
                                    </label>     
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_out" id="7" value="ten_out">
                                    <label class="form-check-label" for="7">
                                    Десятичная 
                                    </label>     
                                </div>                           
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="type_out" id="8" value="sixteen_out">
                                    <label class="form-check-label" for="8">
                                     Шестнадцатеричная
                                    </label>
                                </div>
                                <label for="output">Вывод:  %s</label>
                                <br><button type="submit" class="btn btn-primary">
                                    Конвертировать
                                </button>
                                </form>                           
                            </div>
                          </body>
                        </html>''' % answer
    elif request.method == 'POST':
        answer = ''
        type_in = request.form['type_in']
        type_out = request.form['type_out']
        number_in = request.form['input']
        for i in range(len(number_in)):
            if number_in[i] not in er:
                error_1 = True
        if number_in == '':
            answer = 'Введите число!'
        elif type_in == 'ten_in':
            for i in number_in:
                if i in er[:6]:
                    error_1 = True
                    break
        elif type_in == 'two_in':
            for i in number_in:
                if i not in ['1', '0']:
                    error_1 = True
                    break
        elif type_in == 'eight_in':
            for i in number_in:
                if i not in er[6:14]:
                    error_1 = True
                    break
        if error_1:
            answer = 'Ошбка при вводе значения!'
            error_1 = False
        if answer == "":
            if type_in[:-2] == type_out[:-3]:
                answer = number_in
            else:
                if type_in == 'ten_in':
                    number_in = int(number_in)
                    if type_out == 'two_out':
                        while number_in != 0:
                            buffer.append(str(number_in % 2))
                            number_in //= 2
                        answer = ''.join(buffer[::-1])
                    elif type_out == 'eight_out':
                        while number_in != 0:
                            buffer.append(str(number_in % 8))
                            number_in //= 8
                        answer = ''.join(buffer[::-1])
                    elif type_out == 'sixteen_out':
                        while number_in != 0:
                            buffer.append(str(number_in % 16))
                            if int(buffer[-1]) >= 10:
                                buffer[-1] = dic[int(buffer[-1])]
                            number_in //= 16
                        answer = ''.join(buffer[::-1])
            if type_in == 'two_in':
                if type_out == 'ten_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 2 ** z)
                elif type_out == 'eight_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 2 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 8))
                        answer //= 8
                    answer = ''.join(buffer[::-1])
                elif type_out == 'sixteen_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 2 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 16))
                        if int(buffer[-1]) >= 10:
                            buffer[-1] = dic[int(buffer[-1])]
                        answer //= 16
                    answer = ''.join(buffer[::-1])
            if type_in == 'eight_in':
                if type_out == 'two_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 8 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 2))
                        answer //= 2
                    answer = ''.join(buffer[::-1])
                elif type_out == 'ten_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 8 ** z)
                elif type_out == 'sixteen_out':
                    for z in range(len(number_in)):
                        buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 8 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 16))
                        if int(buffer[-1]) >= 10:
                            buffer[-1] = dic[int(buffer[-1])]
                        answer //= 16
                    answer = ''.join(buffer[::-1])
            if type_in == 'sixteen_in':
                if type_out == 'two_out':
                    for z in range(len(number_in)):
                        if number_in[z].isalpha():
                            buffer.append(str(dic1[number_in[z]]))
                        else:
                            buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 16 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 2))
                        answer //= 2
                    answer = ''.join(buffer[::-1])
                elif type_out == 'eight_out':
                    for z in range(len(number_in)):
                        if number_in[z].isalpha():
                            buffer.append(str(dic1[number_in[z]]))
                        else:
                            buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 16 ** z)
                    buffer.clear()
                    while answer != 0:
                        buffer.append(str(answer % 8))
                        answer //= 8
                    answer = ''.join(buffer[::-1])
                elif type_out == 'ten_out':
                    for z in range(len(number_in)):
                        if number_in[z].isalpha():
                            buffer.append(str(dic1[number_in[z]]))
                        else:
                            buffer.append(number_in[z])
                    buffer = buffer[::-1]
                    answer = 0
                    for z in range(len(buffer)):
                        answer += (int(buffer[z]) * 16 ** z)
        buffer.clear()
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(port=8888, host='127.0.0.1')