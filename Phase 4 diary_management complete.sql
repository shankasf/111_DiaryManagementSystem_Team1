/*drop database diary_management;*/
create database if not exists diary_management;
use diary_management;
-- SET_FOREIGN_CHECKS = 0;
-- SET_FOREIGN_CHECKS = 1;

create table if not exists Admins (
  Admin_ID int primary key,
  Name varchar(25) not null,
  Creation_Date date not null,
  Account_Age int not null,
  Archive_Num int not null
);

insert into Admins(admins_id, admin_name, creation_date, account_age, archive_num) value
(7, 'Jesus', '2024-03-20', 1, 2);
select * from Admins;
TRUNCATE Admins;

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
    on delete cascade
);

insert into Admin_Archives (archive_name, admin_id, creator_type, creator_id, record_id, record_description) value
	('Test Archive', 0001, 'Admin', 0002, 0003, 'A test of the admin_archives table.');
select * from Admin_Archives;
TRUNCATE Admin_Archives; 

create table if not exists Creators (
  Creator_ID int not null primary key,
  Creator_Type enum('User', 'Group') not null default 'User'
 );

insert into Creators (creator_id, creator_type) value (1, 'Admin');
select * from Creators;
TRUNCATE Creators;

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

/*test*/
insert into Users(user_id, has_admin, admin_id, creation_date, account_age) value
(1, 'yes', 7, '2024-03-20', 1);
select * from Users;
TRUNCATE Users;

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
insert into _Groups(Group_ID, Creator_ID, Creation_Date, Group_Age, Member_Num)
values (0,0,curdate(),1,0);
select * from _Groups;
TRUNCATE _Groups;


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

insert into Diaries (diary_id, diary_name, owner_type, owner_id, creation_date, diary_age, record_num, gallery_num) value
(1, 'Diary #1', 'Owner', 321, '2024-03-20', '2024-03-20', 1, 1);
select * from Diaries;
TRUNCATE Diaries;

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

insert into Records (record_id, record_name, diary_id, in_gallery, gallery_id, creation_date, record_age_in_days, record_description) value
(1, 'Test Record',  24, 'No', 42, '2024-03-18', 1, 'A test of the records table');
select * from Records;
TRUNCATE Records;

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
TRUNCATE Galleries;

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

insert into Planners (Planner_ID, Planner_name, Owner_Type, Owner_ID, Creation_Date, Planner_Age, Task_Num, Checklist_Num)
values (0, 'Test Planner', 'User', 0, curdate(), datediff(curdate(),curdate()), 0, 0);
select * from Planners;
TRUNCATE Planners;

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

insert into Tasks (Task_ID, Planner_ID, In_Checklist, Checklist_ID, Creation_Date, Task_Due_Date, Task_Name, Task_Description) 
values (0, 0, 'No', 0, '2024-03-19','2024-03-26', 'Test Task', 'Testing' );
select * from Tasks;
TRUNCATE Tasks;

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
-- test
insert into Checklists (Checklist_ID, Planner_ID, Checklist_Name, Checklist_Age, Task_Num)
values (0, 0, 'Test Checklist', datediff(curdate(), curdate()), 0);
select * from Checklists;
TRUNCATE Checklists;

create table if not exists Admins_Users(
admin_id int,
user_id int,
primary key( admin_id, user_id),
constraint
	foreign key (admin_id)
    references admins(admin_id)
    on delete cascade,
constraint
	foreign key (user_id)
    references users(user_id)
    on delete cascade
);

insert into Admin_Users into (admin_id, user_ID)
values (0,3);
select * from Admin_Users;
TRUNCATE Admin_Users;
