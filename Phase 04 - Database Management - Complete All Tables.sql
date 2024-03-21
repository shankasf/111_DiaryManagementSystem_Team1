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
admin_name varchar(25),
creation_date date,
account_age int,
archive_num int
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
has_admin enum('yes', 'no'),
admin_id int,
creation_date date,
account_age int
);

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

select * from Galleries