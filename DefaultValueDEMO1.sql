CREATE DATABASE school;

USE school;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) DEFAULT 'Anonymous',
    age INT DEFAULT 18,
    enrollment_date DATE DEFAULT (CURRENT_DATE)
);



INSERT INTO students (name) VALUES ('Erick');
INSERT INTO students (age) VALUES (19);
INSERT INTO students (age, enrollment_date) VALUES (19, '2022-09-15');
select * from students;