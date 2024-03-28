/* 
Team 1
3/18/2024
CMPT 308N Section 111 (Database Management)
Phase 4: Complete All Files
*/

create database diary_management;
use diary_management;

create table admins(
admins_id int primary key,
admin_name varchar(25) not null,
creation_date date not null,
account_age int not null,
archive_num int not null
);

/*test*/
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(7, 'Jesus', '2024-03-20', 1, 2);

select * from admins;

create table admin_archives (
	archive_name varchar(25) primary key,
    admin_id int,
    creator_type enum ('Admin', 'User'),
    creator_id int,
    record_id int,
    record_description varchar(255)
);

insert into admin_archives (archive_name, admin_id, creator_type, creator_id, record_id, record_description) value
	('Test Archive', 0001, 'Admin', 0002, 0003, 'A test of the admin_archives table.');
select * from admin_archives;
/* drop table admin_archives */

create table users (
user_id int primary key,
has_admin enum('yes', 'no') not null default 'No',
admins_id int,
foreign key(admins_id) references admins(admins_id),
creation_date date not null,
account_age int not null,
constraint 
	foreign key (user_id)
    references creators (creator_id)
    on delete cascade,
constraint
	foreign key (admins_id)
	references admins(admins_id)
    on delete no action
    on update no action
);
drop table users;

/*test*/
insert into users(user_id, has_admin, admin_id, creation_date, account_age) value
(1, 'yes', 7, '2024-03-20', 1);

select * from users;

create table creators(
	creator_id int primary key,
    creator_type enum ('Creator', 'Admin')
);    

insert into creators (creator_id, creator_type) value (1, 'Admin');

select * from creators;
#drop table creators

create table diaries (
	diary_id int primary key,
    diary_name varchar(25),
    owner_type enum ('Owner', 'Admin'),
    owner_id int,
    creation_date date,
    diary_age date,
    record_num int,
    gallery_num int
);

insert into diaries (diary_id, diary_name, owner_type, owner_id, creation_date, diary_age, record_num, gallery_num) value
	(1, 'Diary #1', 'Owner', 321, '2024-03-20', '2024-03-20', 1, 1);

select * from diaries;
#drop table diaries

create table records (
	record_id int primary key,
	record_name varchar(25),
    diary_id int,
    in_gallery enum('Yes', 'No'),
    gallery_id int,
    creation_date date,
    record_age_in_days int,
    record_description varchar(255)
);

insert into records (record_id, record_name, diary_id, in_gallery, gallery_id, creation_date, record_age_in_days, record_description) value
	(1, 'Test Record',  24, 'No', 42, '2024-03-18', 1, 'A test of the records table');
select * from records;
/* drop table records; */


create table if not exists Planners (
  Planner_ID int not null,
  Planner_Name varchar(25),
  Owner_Type enum('User', 'Group') not null default 'User',
  Owner_ID int not null,
  Creation_Date date not null,
  Planner_Age int not null,
  Task_Num int not null,
  Checklist_Num int not null,
  primary key (Planner_ID, Owner_ID),
  index (Owner_ID asc) visible,
  constraint 
    foreign key (Owner_ID)
    references Creators (Creator_ID)
    on delete cascade
);

-- test
insert into Planners (Planner_ID, Planner_name, Owner_Type, Owner_ID, Creation_Date, Planner_Age, Task_Num, Checklist_Num)
values (0, 'Test Planner', 'User', 0, curdate(), datediff(curdate(),curdate()), 0, 0);

create table if not exists Tasks (
  Task_ID  int not null,
  Planner_ID int not null,
  In_Checklist enum('Yes', 'No') default 'No',
  Checklist_ID int,
  Creation_Date date not null,
  Task_Due_Date date,
  Task_Name varchar(25) ,
  Task_Description varchar(255),
  primary key (Task_ID, Planner_ID),
  index (Planner_ID asc) visible, 
  constraint 
    foreign key (Planner_ID)
    references Planners (Planner_ID)
    on delete cascade
);

-- test
insert into Tasks (Task_ID, Planner_ID, In_Checklist, Checklist_ID, Creation_Date, Task_Due_Date, Task_Name, Task_Description) 
values (0, 0, 'No', 0, '2024-03-19','2024-03-26', 'Test Task', 'Testing' );

select * from Tasks;

create table if not exists Galleries (
  Gallery_ID int not null,
  Diary_ID int not null,
  Owner_Type enum('User', 'Group') default 'User',
  Owner_ID int not null,
  Creation_Date date not null,
  Gallery_Name varchar(25),
  Gallery_Age int not null,
  Record_Num int not null,
  primary key (Gallery_ID, Diary_ID),
  index (Diary_ID asc) visible,
  constraint
    foreign key (Diary_ID)
    references Diaries (Diary_ID)
    on delete cascade
);

-- test
insert into Galleries (Gallery_ID, Diary_ID, Owner_Type, Owner_ID, Creation_Date, Gallery_Name, Gallery_Age, Record_Num)
values (0, 0, 'User', 0, curdate(), 'Test Gallery', datediff(curdate(), curdate()), 0);

select * from Galleries;


create table if not exists Admins_Users(
admins_id int primary key,
user_id int,
constraint
	foreign key (admins_id)
    references admins(admins_id)
    on delete cascade,
constraint
	foreign key (user_id)
    references users(user_id)
    on delete cascade
);

select * from admins_users;

/* Phase 05 Starts*/

show tables;

select * from admins;

insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(7, 'Jesus', '2024-03-20', 1, 2);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(6, 'Solomon', '2024-12-17', 1, 6);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(11, 'Cayleigh', '2024-01-11', 1, 11);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(8, 'Erik', '2024-02-17', 1, 8);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(9, 'Cheryl', '2024-03-19', 1, 9);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(10, 'Jakie', '2003-03-16', 21, 10);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(1, 'Sandra', '2002-12-17', 21, 1);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(2, 'Jovanna', '2003-11-28', 20, 2);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(3, 'Melanie', '2003-07-30', 20, 3);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(4, 'Lesly', '2003-04-10', 20, 4);
insert into admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(5, 'Jalen', '2002-03-27', 22, 5);


select * from users;

SET FOREIGN_KEY_CHECKS = 0;
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(1, 'yes', 7, '2024-03-20', 1);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(2, 'no', null, '2024-03-01', 1);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(3, 'yes', 5, '2024-03-02', 1);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(4, 'no', null, '2022-03-01', 2);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(5, 'yes', 7, '2020-03-08', 4);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(6, 'no', null, '2024-03-10', 1);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(7, 'yes', 8, '2021-01-06', 3);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(8, 'yes', 10, '2024-03-16', 1);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(9, 'no', null, '2021-03-18', 3);
insert into users(user_id, has_admin, admins_id, creation_date, account_age) value
(10, 'yes', 2, '2021-04-18', 3);

select user_id from users where user_id > 5 order by user_id;

select user_id from users full join admins where user_id > 8;


