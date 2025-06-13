create database project;
use  project;
create table login(
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
select * from login;
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);


CREATE TABLE student_attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    register_no VARCHAR(20) NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL
);
select * from student_attendance;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    register_number VARCHAR(50) UNIQUE NOT NULL,
    shift ENUM('A', 'B') NOT NULL
);
select *from students;
INSERT INTO students (student_name, roll_number, course, shift)
VALUES ('Alice Johnson', '2023001', 'Computer Science', 'Morning');

CREATE TABLE attendance_search (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    shift VARCHAR(50) NOT NULL,
    attendance_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
show tables;
-- Departments table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

-- Shifts table
CREATE TABLE shifts (
    shift_id INT AUTO_INCREMENT PRIMARY KEY,
    shift_name VARCHAR(50) NOT NULL UNIQUE
);

-- Attendance records table
CREATE TABLE att (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    department_id INT NOT NULL,
    shift_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (shift_id) REFERENCES shifts(shift_id)
);
show tables;
describe login;
insert into login values(1,'divya kumar', '1234');
select * from login;
CREATE DATABASE project;
USE project;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    register_number VARCHAR(20)
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    status ENUM('Present', 'Absent'),
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
show tables;
select * from attendance;
select * from students;
INSERT INTO attendance (student_id, status, date) VALUES
(1, 'Present', '2025-06-07'),
(2, 'Absent', '2025-06-07'),
(3, 'Present', '2025-06-07'),
(4, 'Present', '2025-06-07'),
(5, 'Absent', '2025-06-07'),
(6, 'Present', '2025-06-07');

INSERT INTO students (name, register_number) VALUES
('divya kumar', '2023001'),
('Praveen', '2023002'),
('Navanee', '2023003'),
('Nithyasri', '2023004'),
('azhagu ganesh', '2023005'),
('abishek', '2023006');




