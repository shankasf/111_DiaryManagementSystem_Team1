/* 
Team 1
4/3/2024
CMPT 308N Section 111 (Database Management)
Phase 6
*/
drop database diary_management;
create database if not exists diary_management;
use diary_management;

create table if not exists Admins (
Admins_ID int primary key,
Admin_name varchar(25) not null,
Creation_Date date not null,
Account_age int not null,
Archive_num int not null
);

create table if not exists Admin_Users (
Admin_ID int,
Creator_ID int,
Adminee_Status enum ('Requested', 'Established') default 'Requested'
primary key (Admin_ID, Creator_ID)
constraint
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete cascade,
constraint
    foreign key (Creator_ID)
    references Creator(Creator_ID)
    on delete cascade
);

create table if not exists Admin_Archives (
Admin_ID int not null,
Creator_ID int not null,
Record_ID int not null, 
Record_Description varchar(255),
primary key (Admin_ID, Creator_ID, Record_ID),
constraint 
  foreign key (Admin_ID)
  references Admins(Admin_ID)
  on delete cascade
);

create table if not exists Users (
  User_ID int primary key,
  Username varchar(25) unique,
  Password varchar(25),
  Has_Admin enum('Yes', 'No') not null default 'No',
  Admin_ID int,
  Creation_Date date not null,
  Account_Age int not null,
  constraint
    foreign key (User_ID)
    references Creators (Creator_ID)
    on delete cascade,
  constraint
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete no action
    on update no action
);

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


create table if not exists Creators (
  Creator_ID int not null primary key,
  Creator_Type enum('User', 'Group') not null default 'User'
 );

create table if not exists Diaries (
Diary_ID int not null,
Diary_Name varchar(25),
Owner_Type enum('User', 'Group') not null default 'User',
Owner_ID int not null,
Creation_Date date not null,
Diary_Age int not null,
Record_Num int not null,
Gallery_Num int not null,
  primary key (Diary_ID, Owner_ID),
  constraint 
    foreign key (Owner_ID)
    references Creators (Creator_ID)
    on delete cascade
);

create table if not exists Records (
Record_ID int not null,
Diary_ID int not null,
In_Gallery enum('Yes','No') default 'No',
Gallery_ID int,
Record_Age int not null,
Record_Name varchar(25),
primary key (Record_ID, Diary_ID),
constraint 
  foreign key (Diary_ID)
  references Diaries (Diary_ID)
  on delete cascade
);

create table if not exists Galleries (
Gallery_ID int not null,
Diary_ID int not null,
Owner_Type enum('User', 'Default') default 'User',
Creation_Date date not null, 
Gallery_Name varchar(25),
Gallery_Age int not null, 
Record_Num int not null,
primary key (Gallery_ID, Diary_ID),
constraint 
  foreign key (Diary_ID)
  references Diaries (Diary_ID)
  on delete cascade
);

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
  constraint 
    foreign key (Owner_ID)
    references Creators (Creator_ID)
    on delete cascade
);

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
  constraint 
    foreign key (Planner_ID)
    references Planners (Planner_ID)
    on delete cascade
);

create table if not exists Checklists (
  Checklist_ID int not null,
  Planner_ID int not null,
  Checklist_Name varchar(25),
  Checklist_Age int not null,
  Task_Num int not null,
  primary key (Checklist_ID, Planner_ID),
  constraint
    foreign key (Planner_ID)
    references Planners (Planner_ID)
    on delete cascade
);
