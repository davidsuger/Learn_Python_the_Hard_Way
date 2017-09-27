from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from learn import planisphere

app = Flask(__name__)
app.debug = 1


@app.route('/')
def index():
    session['room_name'] = planisphere.START
    return redirect(url_for('game'))


@app.route('/game', methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template('show_room.html', room=room)
        else:
            return render_template('you_died.html')
    else:
        action = request.form.get('action')
        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
    return redirect(url_for('game'))


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet},{name}'
        return render_template('index.html', greeting=greeting)
    else:
        return render_template('hello_form.html')


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()
