/*
Team 1
29 February 2024
CMPT 308N, Section 111
Phase 03: Default Value Insertion & Implicit Default Handling Examples
*/

/* To turn off strict mode, use the first command. To turn on strict mode use the second command
SET SESSION sql_mode = '';
SET SESSION sql_mode = 'strict_all_tables'

*/
CREATE DATABASE school;
USE school;

CREATE TABLE students (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) DEFAULT 'Anonymous',
    age INT DEFAULT 18,
    enrollment DATE DEFAULT (CURDATE())
);

--  Default Value Insertion
INSERT INTO students VALUES();
INSERT INTO students VALUES(DEFAULT,DEFAULT,DEFAULT,DEFAULT);
INSERT INTO students VALUES (DEFAULT(id), DEFAULT(name), Default(age), CURDATE());

SELECT * FROM students;
TRUNCATE students;

-- Implicit Default Handling
ALTER TABLE students
MODIFY COLUMN age INT; -- DEFAULT NULL

-- Default value for age is now null
INSERT INTO students VALUES(); 
INSERT INTO students VALUES(DEFAULT,DEFAULT,DEFAULT,DEFAULT);
INSERT INTO students VALUES (DEFAULT(id), DEFAULT(name), Default(age), CURDATE());

SELECT * FROM students;
TRUNCATE students;

-- Implicit Default Handling (Not Null)
ALTER TABLE students
MODIFY COLUMN age INT NOT NULL; -- NO DEFAULT CLAUSE

INSERT INTO students VALUES();
INSERT INTO students VALUES(DEFAULT,DEFAULT,DEFAULT,DEFAULT);
INSERT INTO students VALUES (DEFAULT(id), DEFAULT(name), Default(age), CURDATE()); -- Default function returns error

SELECT * FROM students;
TRUNCATE students;
/* 
If SQL Strict mode is enabled
Then Error 1364, 'no default value', will be returned 
and no new record will be made
*/

/* 
If SQL Strict mode isn't enabled
Then Warning 1364, 'no default value', will be returned 
and the data type's implicit default value will be used instead

*/
