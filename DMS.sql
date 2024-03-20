drop database Project_DMS;
create database if not exists Project_DMS;
use Project_DMS;

create table if not exists Admins (
  Admin_ID int primary key,
  Name varchar(25) not null,
  Creation_Date date not null,
  Account_Age int not null,
  Archive_Num int not null
);

create table if not exists Admin_Archives (
  Archive_Name varchar(25) not null,
  Admin_ID int not null,
  Creator_Type enum('User', 'Group') not null default 'User',
  Creator_ID int not null,
  Record_ID int not null,
  Record_Description varchar(255),
  primary key (Archive_Name, Admin_ID),
  index (`Admin_ID` asc) visible,
  constraint 
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete cascade);

create table if not exists Creators (
  Creator_ID int not null primary key,
  Creator_Type enum('User', 'Group') not null default 'User'
 );

create table if not exists Users (
  User_ID int not null,
  Has_Admin enum('Yes', 'No') not null default 'No',
  Admin_ID int,
  Creation_Date date not null,
  Account_Age int not null,
  primary key (User_ID),
  index (Admin_ID asc) visible,
  constraint
    foreign key (User_ID)
    references Creators (Creator_ID)
    on delete cascade,
  constraint
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete no action
    on update no action);

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

create table if not exists Records (
  Record_ID int not null,
  Diary_ID int not null,
  In_Gallery enum('Yes', 'No') default 'No',
  Galley_ID int,
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
