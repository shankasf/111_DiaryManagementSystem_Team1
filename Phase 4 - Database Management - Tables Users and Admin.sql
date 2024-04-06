/* 
Team 1
3/20/2024
CMPT 308N Section 111 (Database Management)
Phase 4: Users and Admins
*/

create database diary_management;
use diary_management;


create table users (
user_id int primary key,
has_admin enum('yes', 'no'),
admin_id int,
creation_date date,
account_age int
);

/*test*/
insert into users(user_id, has_admin, admin_id, creation_date, account_age) value
(1, 'yes', 7, '2024-03-20', 1);

select * from users;

create table admins(
admins_id int primary key,
admin_name varchar(25),
creation_date date,
account_age int,
archive_num int
);

/*test*/
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(7, 'Jesus', '2024-03-20', 1, 2);

select * from admins;


