from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Digidara1000@",  # Replace with your actual password
    database="project"
)
cursor = db.cursor(dictionary=True)  # Enable dictionary cursor to use keys

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Department Selection Page
@app.route('/departmentmod')
def departmentmod():
    return render_template("departmentmod.html")

@app.route('/subject')
def subject():
    return render_template("subject.html")

# Login Page (GET)
@app.route('/login')
def login():
    return render_template("login.html")

# Login Form Submit (POST)
@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        return redirect(url_for('attendance'))
    else:
        return "<h3 style='color:red;'>❌ Invalid credentials!</h3><br><a href='/login'>Try again</a>"

# Attendance Form Page
@app.route('/attendance', methods=['GET'])
def attendance():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("attendance.html", students=students)

# Submit Attendance (POST)
@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    attendance_date = request.form.get("attendance_date")
    
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        student_id = student['id']
        status = request.form.get(f'attendance_{student_id}')
        if status:
            cursor.execute("""
                INSERT INTO attendance (student_id, status, date)
                VALUES (%s, %s, %s)
            """, (student_id, status, attendance_date))

    db.commit()
    return redirect(url_for('success'))

# Success Page
@app.route('/success')
def success():
    return "<h2 style='text-align:center;'>✅ Attendance Submitted Successfully!</h2><br><a href='/'>Go Home</a>"

# View Attendance Page
@app.route('/view')

def view():
    cursor.execute("SELECT * FROM attendance ORDER BY date DESC, student_id ASC")
    records = cursor.fetchall()
    return render_template("view.html", records=records)
@app.route('/newentry')
def newentry():
    return render_template("newentry.html")

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    register_number = request.form['roll_no']
    course = request.form['course']
    # shift = request.form['shift']

    cursor.execute("""
        INSERT INTO add_student (name, registernumber, course)
        VALUES ( %s, %s, %s)
    """, (name, register_number, course))
    db.commit()
    return render_template("memo.html")

@app.route('/memo')
def memo():
    return render_template("memo.html")



if __name__ == '__main__':
    app.run(debug=True)
