from flask import Blueprint, render_template, request, redirect
import sqlite3


views = Blueprint("views", __name__)


def create_DB():
    pass

@views.route('/', methods=['GET', 'POST'])
def home():

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Liquor_anniversary_TB')
        datas = cursor.fetchall()

    return render_template('home.html', datas=datas)

@views.route('/add')
def add():
    return render_template('from.html')

@views.route('/submit', methods=['GET', 'POST'])
def submit_data():
    if request.method == 'POST':
        detail = request.form['detail']
        full_name = request.form['full_name']
        position = request.form['position']
        Agency = request.form['Agency']
        with sqlite3.connect("database.db") as conn:
            if not detail or not full_name:
                return render_template('from.html', error='กรุณากรอกทุกช่อง')
            else:
                cur = conn.cursor()
                sql = '''INSERT INTO Liquor_anniversary_TB(Detail, Full_name, Position, Agency)
                        VALUES(?, ?, ?, ?)'''
                cur.execute(sql, (detail, full_name, position, Agency))
                conn.commit()
                print('Add data complete !!!!!')
                # conn.close()
    return redirect('/')


@views.route('/delete')
def delete():
    id_data = request.args.get('id')
    if not id_data:
        return redirect('/')
    else:
        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            sql = '''DELETE FROM Liquor_anniversary_TB WHERE Id = ?'''
            cur.execute(sql, (id_data, ))
            conn.commit()
    return redirect('/')
