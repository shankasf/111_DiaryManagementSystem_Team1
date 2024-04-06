/* 
Team 1
3/28/2024
CMPT 308N Section 111 (Database Management)
Phase 5: Creators, Diaries, _Groups, Galleries, Planners, Tasks, and Checklists
*/

create database if not exists diary_management;
use diary_management;
-- drop database diary_management;
-- set foreign_key_checks = 0;
-- set foreign_key_checks = 1;

-- Admins
create table if not exists Admins(
  Admins_ID int primary key,
  Admin_name varchar(25) not null,
  Creation_date date not null,
  Account_age int not null,
  Archive_num int not null
);

insert into Admins(Admins_ID, Admin_name, Creation_date, Account_age, Archive_num) values
(7, 'Jesus', '2024-03-20', 1, 2),
(6, 'Solomon', '2024-12-17', 1, 6),
(11, 'Cayleigh', '2024-01-11', 1, 11),
(8, 'Erik', '2024-02-17', 1, 8),
(9, 'Cheryl', '2024-03-19', 1, 9),
(10, 'Jakie', '2003-03-16', 21, 10),
(1, 'Sandra', '2002-12-17', 21, 1),
(2, 'Jovanna', '2003-11-28', 20, 2),
(3, 'Melanie', '2003-07-30', 20, 3),
(4, 'Lesly', '2003-04-10', 20, 4,
(5, 'Jalen', '2002-03-27', 22, 5);
select * from Admins;

-- Admin_Archives
create table if not exists Admin_Archives (
  Admin_ID int not null,
  Creator_ID int not null,
  Record_ID int not null,
  Record_Description varchar(255),
  primary key (Admin_ID, Creator_ID, Record_ID),
  index (`Admin_ID` asc) visible,
  constraint 
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete cascade
);

insert into Admin_Archives(Admin_ID, Creator_type, Creator_ID, Record_description) values
(42, 54, 8, 'A collection of old patch notes for reference purposes'),
(26, 26, 12, 'User accounts that may have broken broken community guidelines'),
(29, 2, 13, 'User accounts that have broken community guidelines once'),
(10, 2, 12, 'User accounts that have broken community guidelines twice'),
(3, 2, 11, 'A list of banned accounts, or user accounts that have broken community guidelines three times'),
(32, 18, 101, 'Accounts that have not had activity for a year or more'),
(12, 119, 135, 'Copy of the publicly available community guidelines'),
(14, 47, 123, 'Viable User and Admin suggestions to include in new updates'),
(27, 20, 74, 'General files that may be useful for later reference'),
(38, 38, 137, 'Additional notes that are important for Admins, but do not fit anywhere else');
Select * from Admin_Archives;

-- Creators
create table if not exists Creators (
  Creator_ID int not null primary key,
  Creator_Type enum('User', 'Group') not null default 'User'
 );
 
insert into Creators (Creator_ID, Creator_Type) values
(1, 'User'),
(2, 'Group'),
(3, 'User'),
(4, 'Group'),
(5, 'User'),
(6, 'Group'),
(7, 'User'),
(8, 'Group'),
(9, 'User'),
(10, 'Group');
select * from Creators;

-- Diaries
create table if not exists Diaries (
  Diary_ID int not null,
  Diary_Name varchar(25),
  Owner_Type enum('User', 'Group') not null default 'User',
  Owner_ID int not null,
  Creation_Date date not null,
  Diary_Age int not null,
  Record_Num int not null,
  Gallery_Num int not null,
  primary key (`Diary_ID`, `Owner_ID`),
  index (`Owner_ID` asc) visible,
  constraint
    foreign key (`Owner_ID`)
    references Creators (Creator_ID)
    on delete cascade
);

insert into Diaries (Diary_ID, Diary_Name, Owner_Type, Owner_ID, Creation_Date, Diary_Age, Record_Num, Gallery_Num) values
(1, 'Personal Diary', 'User', 1, '2024-01-01', 1, 5, 3),
(2, 'Work Diary', 'User', 2, '2024-02-01', 1, 10, 5),
(3, 'Family Diary', 'Group', 1, '2024-03-01', 1, 8, 4),
(4, 'Travel Diary', 'Group', 2, '2024-04-01', 1, 12, 6),
(5, 'Fitness Diary', 'User', 3, '2024-05-01', 1, 7, 2),
(6, 'Study Diary', 'Group', 3, '2024-06-01', 1, 15, 8),
(7, 'Recipe Diary', 'User', 4, '2024-07-01', 1, 6, 3),
(8, 'Art Diary', 'Group', 4, '2024-08-01', 1, 9, 4),
(9, 'Project Diary', 'User', 5, '2024-09-01', 1, 11, 7),
(10, 'Event Diary', 'Group', 5, '2024-10-01', 1, 13, 5);
select * from Diaries;

-- Users
create table Users (
User_id int primary key,
Has_admin enum('Yes', 'No') not null default 'No',
Admins_ID int,
foreign key(Admins_id) references Admins(Admins_id),
Creation_date date not null,
Account_age int not null,
constraint 
	foreign key (User_id)
    references Creators (Creator_id)
    on delete cascade,
constraint
	foreign key (Admins_id)
	references Admins(Admins_id)
    on delete no action
    on update no action
);

insert into Users(User_id, Has_admin, Admins_ID,  Creation_date, Account_age) values
(1, 'Yes', 7, '2024-03-20', 1),
(2, 'Yes', null, '2024-03-01', 1),
(3, 'Yes', 5, '2024-03-02', 1),
(4, 'No', null, '2022-03-01', 2),
(5, 'Yes', 7, '2020-03-08', 4),
(6, 'No', null, '2024-03-10', 1),
(7, 'Yes', 8, '2021-01-06', 3),
(8, 'Yes', 10, '2024-03-16', 1),
(9, 'No', null, '2021-03-18', 3),
(10, 'Yes', 2, '2021-04-18', 3);
Select * from Users;

-- _Groups
create table if not exists _Groups (
  Group_ID int not null primary key,
  Creator_ID int not null,
  Creation_Date date not null,
  Group_Age int not null,
  Member_Num int not null,
  constraint
    foreign key (Group_ID)
    references Creators (Creator_ID)
    on delete cascade
);


insert into _Groups (Group_ID, Creator_ID, Creation_Date, Group_Age, Member_Num) values
(1, 1, '2022-01-01', 2, 5),
(2, 2, '2022-02-05', 3, 8),
(3, 3, '2022-03-10', 1, 4),
(4, 4, '2022-04-15', 5, 10),    
(5, 5, '2022-05-20', 4, 7),
(6, 6, '2022-06-25', 2, 6),
(7, 7, '2022-07-30', 3, 9),
(8, 8, '2022-08-05', 6, 12),
(9, 9, '2022-09-10', 2, 5),
(10, 10, '2022-10-15', 4, 8);
select * from _Groups;

-- Records
create table if not exists Records (
  Record_ID int not null,
  Diary_ID int not null,
  In_Gallery enum('Yes', 'No') default 'No',
  Gallery_ID int,
  Creation_Date date not null,
  Record_Age int not null,
  Record_Name varchar(25),
  Record_Description varchar(255),
  primary key (Record_ID, Diary_ID),
  index (Diary_ID asc) visible,
  constraint 
    foreign key (Diary_ID)
    references Diaries (Diary_ID)
	on delete cascade
);

insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
(10, 1, 'Yes', 6, '2024-01-01', 86, 'Cooking Diaries', 'Diaries about various cooking topics'),
(21, 2, 'No', 13, '2024-01-15', 72, 'Personal Diaries', 'General personal diaries that only the creator can view'),
(32, 3, 'Yes', 18, '2024-01-26', 61, 'Workout Diaries', 'Diaries detailing workout routines'),
(43, 4, 'Yes', 25, '2024-02-07', 49, 'Wonderful World of Pets', 'Diaries about pets'),
(54, 5, 'No', 32, '2024-02-12', 44, 'Recovery', 'Personal diaries detailing the physical or mental recovery process of their creator'),
(65, 6, 'Yes', 47, '2024-02-20', 36, 'Poems', 'Diaries showcasing poetry'),
(76, 7, 'No', 54, '2024-02-29', 27, 'Venting', 'Private diaries for venting negative emotions'),
(87, 8, 'Yes', 66, '2024-03-01', 26, 'Mechanics', 'Diaries that explore and exhibit how to fix various mechanical issues'),
(98, 9, 'Yes', 71, '2024-03-13', 14, 'Holidays', 'Diaries dedicated to various holidays'),
(100, 10, 'Yes', 80, '2024-03-21', 6, 'College Diaries', 'Diaries documenting the college experiences of their creators');
Select * from Records;

-- Galleries
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


insert into Galleries (Gallery_ID, Diary_ID, Owner_Type, Owner_ID, Creation_Date, Gallery_Name, Gallery_Age, Record_Num) values
(1, 1, 'User', 1, '2024-01-01', 'Gallery 1', 2, 5),
(2, 2, 'Group', 1, '2024-02-05', 'Gallery 2', 3, 8),
(3, 3, 'User', 2, '2024-03-10', 'Gallery 3', 1, 4),
(4, 4, 'Group', 2, '2024-04-15', 'Gallery 4', 5, 10),
(5, 5, 'User', 3, '2024-05-20', 'Gallery 5', 4, 7),
(6, 6, 'Group', 3, '2024-06-25', 'Gallery 6', 2, 6),
(7, 7, 'User', 4, '2024-07-30', 'Gallery 7', 3, 9),
(8, 8, 'Group', 4, '2024-08-05', 'Gallery 8', 6, 12),
(9, 9, 'User', 5, '2024-09-10', 'Gallery 9', 2, 5),
(10, 10, 'Group', 5, '2024-10-15', 'Gallery 10', 4, 8);
select * from Galleries;

-- Planners
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


insert into Planners (Planner_ID, Planner_Name, Owner_Type, Owner_ID, Creation_Date, Planner_Age, Task_Num, Checklist_Num) values
(1, 'Planner 1', 'User', 1, '2024-01-01', 2, 5, 3),
(2, 'Planner 2', 'Group', 1, '2024-02-05', 3, 8, 4),
(3, 'Planner 3', 'User', 2, '2024-03-10', 1, 4, 2),
(4, 'Planner 4', 'Group', 2, '2024-04-15', 5, 10, 6),
(5, 'Planner 5', 'User', 3, '2024-05-20', 4, 7, 5),
(6, 'Planner 6', 'Group', 3, '2024-06-25', 2, 6, 3),
(7, 'Planner 7', 'User', 4, '2024-07-30', 3, 9, 4),
(8, 'Planner 8', 'Group', 4, '2024-08-05', 6, 12, 7),
(9, 'Planner 9', 'User', 5, '2024-09-10', 2, 5, 2),
(10, 'Planner 10', 'Group', 5, '2024-10-15', 4, 8, 5);
select * from Planners;

-- Tasks
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


insert into Tasks (Task_ID, Planner_ID, In_Checklist, Checklist_ID, Creation_Date, Task_Due_Date, Task_Name, Task_Description) values
(1, 1, 'Yes', 1, '2024-01-01', '2024-01-15', 'Task 1', 'Description for Task 1'),
(2, 2, 'No', 2, '2024-02-05', '2024-02-20', 'Task 2', 'Description for Task 2'),
(3, 3, 'Yes', 3, '2024-03-10', '2024-03-25', 'Task 3', 'Description for Task 3'),
(4, 4, 'No', 4, '2024-04-15', '2024-04-30', 'Task 4', 'Description for Task 4'),
(5, 5, 'Yes', 5, '2024-05-20', '2024-06-05', 'Task 5', 'Description for Task 5'),
(6, 6, 'Yes', 6, '2024-06-25', '2024-07-10', 'Task 6', 'Description for Task 6'),
(7, 7, 'No', 7, '2024-07-30', '2024-08-15', 'Task 7', 'Description for Task 7'),
(8, 8, 'No', 8, '2024-08-05', '2024-08-20', 'Task 8', 'Description for Task 8'),
(9, 9, 'Yes', 9, '2024-09-10', '2024-09-25', 'Task 9', 'Description for Task 9'),
(10, 10, 'Yes', 10, '2024-10-15', '2024-10-30', 'Task 10', 'Description for Task 10');
select * from Tasks;

-- Checklists
create table if not exists Checklists (
  Checklist_ID int not null,
  Planner_ID int not null,
  Checklist_Name varchar(25),
  Checklist_Age int not null,
  Task_Num int not null,
  primary key (Checklist_ID, Planner_ID),
  index (Planner_ID asc) visible,
  constraint
    foreign key (Planner_ID)
    references Planners (Planner_ID)
    on delete cascade
);


insert into Checklists (Checklist_ID, Planner_ID, Checklist_Name, Checklist_Age, Task_Num) values
(1, 1, 'Checklist 1', 2, 5),
(2, 2, 'Checklist 2', 3, 8),
(3, 3, 'Checklist 3', 1, 4),
(4, 4, 'Checklist 4', 5, 10),
(5, 5, 'Checklist 5', 4, 7),
(6, 6, 'Checklist 6', 2, 6),
(7, 7, 'Checklist 7', 3, 9),
(8, 8, 'Checklist 8', 6, 12),
(9, 9, 'Checklist 9', 2, 5),
(10, 10, 'Checklist 10', 4, 8);
select * from Checklists;
