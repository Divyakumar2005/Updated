from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

#MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Digidara1000",  # Replace with your actual password
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
    cursor.execute("""
        SELECT 
            a.id AS id,
            a.student_id,
            s.name AS student_name,
            a.date,
            a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC, a.student_id ASC
    """)
    records = cursor.fetchall()
    return render_template("view.html", records=records)


# Show the Add Student Form (GET)
@app.route('/newentry', methods=['GET'])
def show_newentry_form():
    return render_template("newentry.html")

# Handle the submitted form (POST)
@app.route('/newentry', methods=['POST'])
def newentry():
    name = request.form['name']
    register_number = request.form['roll_no']

    cursor.execute("""
        INSERT INTO students (name, register_number)
        VALUES (%s, %s)
    """, (name, register_number))
    db.commit()
    return redirect(url_for('memo'))

    db.commit()
    return render_template("memo.html")

@app.route('/attendance')
def show_attendance():
    query = """
        SELECT s.id AS student_id, s.name, s.register_number, a.date, a.status
        FROM students s
        JOIN attendance a ON s.id = a.student_id
        ORDER BY a.date DESC
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    # conn.close()
    return render_template('attendance.html', records=data)

@app.route('/memo')
def memo():
    return render_template("memo.html")
@app.route('/merged-attendance')
def merged_attendance():
    query = """
        SELECT 
            a.id AS attendance_id,
            s.id AS student_id,
            s.name AS student_name,
            s.register_number,
            a.date,
            a.status
        FROM 
            attendance a
        JOIN 
            students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('merged_attendance.html', data=data)



if __name__ == '__main__':
    app.run(port=5444,debug=True)
