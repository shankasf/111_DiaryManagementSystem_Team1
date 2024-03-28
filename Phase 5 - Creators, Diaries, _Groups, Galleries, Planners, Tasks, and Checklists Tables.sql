/* 
Team 1
3/28/2024
CMPT 308N Section 111 (Database Management)
Phase 5: Creators, Diaries, _Groups, Galleries, Planners, Tasks, and Checklists
*/

create database if not exists diary_management;
use diary_management;
# drop database diary_management;

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
(3, 3, 'Yes', 3 , '2024-03-10', '2024-03-25', 'Task 3', 'Description for Task 3'),
(4, 4, 'No', 4 , '2024-04-15', '2024-04-30', 'Task 4', 'Description for Task 4'),
(5, 5, 'Yes', 5 , '2024-05-20', '2024-06-05', 'Task 5', 'Description for Task 5'),
(6, 6, 'Yes', 6 , '2024-06-25', '2024-07-10', 'Task 6', 'Description for Task 6'),
(7, 7, 'No', 7, '2024-07-30', '2024-08-15', 'Task 7', 'Description for Task 7'),
(8, 8, 'No', 8, '2024-08-05', '2024-08-20', 'Task 8', 'Description for Task 8'),
(9, 9, 'Yes', 9, '2024-09-10', '2024-09-25', 'Task 9', 'Description for Task 9'),
(10, 10, 'Yes', 10, '2024-10-15', '2024-10-30', 'Task 10', 'Description for Task 10');
select * from Tasks;


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