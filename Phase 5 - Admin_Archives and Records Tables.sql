/* 
Team 1
3/27/2024
CMPT 308N Section 111 (Database Management)
Phase 5: Admin_Archives and Records
*/

create database diary_management;
use diary_management;

/* drop database diary_management; */

-- Necessary Tables for Setup Purposes (Admin_Archives and Records reference these tables)
create table if not exists Admins (
  Admin_ID int primary key,
  Name varchar(25) not null,
  Creation_Date date not null,
  Account_Age int not null,
  Archive_Num int not null
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
  primary key (`Diary_ID`, `Owner_ID`),
  index (`Owner_ID` asc) visible,
  constraint
    foreign key (`Owner_ID`)
    references Creators (Creator_ID)
    on delete cascade
);
-- End of Reference Tables

-- Admin_Archives
create table if not exists Admin_Archives (
  Archive_Name varchar(25) not null,
  Admin_ID int not null,
  Creator_ID int not null,
  Record_ID int not null,
  Record_Description varchar(255),
  primary key (Archive_Name, Admin_ID),
  index (`Admin_ID` asc) visible,
  constraint 
    foreign key (Admin_ID)
    references Admins (Admin_ID)
    on delete cascade);

select * from Admin_Archives;
-- drop table Admin_Archives;
set foreign_key_checks = 0;
-- Insert Statements
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_ID, Record_ID, Record_Description) value
	('Old Patch Notes', 42, 54, 8, 'A collection of old patch notes for reference purposes'),
    ('Marked for Review', 26, 26, 12, 'User accounts that may have broken broken community guidelines'),
    ('One Strike', 29, 2, 13, 'User accounts that have broken community guidelines once'),
    ('Two Strikes', 10, 2, 12, 'User accounts that have broken community guidelines twice'),
    ('Banned Accounts', 3, 2, 11, 'A list of banned accounts, or user accounts that have broken community guidelines three times'),
    ('Inactive Accounts', 32, 18, 101, 'Accounts that have not had activity for a year or more'),
    ('Community Guidelines Copy', 12, 119, 135, 'Copy of the publicly available community guidelines'),
    ('New Update Suggestions', 14, 47, 123, 'Viable User and Admin suggestions to include in new updates'),
    ('Reference Files', 27, 20, 74, 'General files that may be useful for later reference'),
    ('General Notes', 38, 38, 137, 'Additional notes that are important for Admins, but do not fit anywhere else');

insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
    ('Old Patch Notes', 42, 'Group', 54, 8, 'A collection of old patch notes for reference purposes');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Marked for Review', 26, 'User', 26, 12, 'User accounts that may have broken broken community guidelines');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('One Strike', 29, 'User', 2, 13, 'User accounts that have broken community guidelines once');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Two Strikes', 10, 'User', 2, 12, 'User accounts that have broken community guidelines twice');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Banned Accounts', 3, 'User', 2, 11, 'A list of banned accounts, or user accounts that have broken community guidelines three times');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Inactive Accounts', 32, 'User', 18, 101, 'Accounts that have not had activity for a year or more');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Community Guidelines Copy', 12, 'Group', 119, 135, 'Copy of the publicly available community guidelines');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('New Update Suggestions', 14, 'Group', 47, 123, 'Viable User and Admin suggestions to include in new updates');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('Reference Files', 27, 'Group', 20, 74, 'General files that may be useful for later reference');
insert into Admin_Archives (Archive_Name, Admin_ID, Creator_Type, Creator_ID, Record_ID, Record_Description) value
	('General Notes', 38, 'Group', 38, 137, 'Additional notes that are important for Admins, but do not fit anywhere else');
    
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

select * from Records;
drop table Records;
set foreign_key_checks = 0;
-- Insert Statements
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

insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(10, 1, 'Yes', 6, '2024-01-01', 86, 'Cooking Diaries', 'Diaries about various cooking topics');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(21, 2, 'No', 13, '2024-01-15', 72, 'Personal Diaries', 'General personal diaries that only the creator can view');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(32, 3, 'Yes', 18, '2024-01-26', 61, 'Workout Diaries', 'Diaries detailing workout routines');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(43, 4, 'Yes', 25, '2024-02-07', 49, 'Wonderful World of Pets', 'Diaries about pets');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(54, 5, 'No', 32, '2024-02-12', 44, 'Recovery', 'Personal diaries detailing the physical or mental recovery process of their creator');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(65, 6, 'Yes', 47, '2024-02-20', 36, 'Poems', 'Diaries showcasing poetry');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(76, 7, 'No', 54, '2024-02-29', 27, 'Venting', 'Private diaries for venting negative emotions');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(87, 8, 'Yes', 66, '2024-03-01', 26, 'Mechanics', 'Diaries that explore and exhibit how to fix various mechanical issues');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(98, 9, 'Yes', 71, '2024-03-13', 14, 'Holidays', 'Diaries dedicated to various holidays');
insert into Records (Record_ID, Diary_ID, In_Gallery, Gallery_ID, Creation_Date, Record_Age, Record_Name, Record_Description) value
	(100, 10, 'Yes', 80, '2024-03-21', 6, 'College Diaries', 'Diaries documenting the college experiences of their creators');
    
    
    
    
    
    
    
    
-- Views describe tables that might need to be joined. For example, both username and password have to be
-- analyzed for login. If they were in separate tables, the tables would need to be combined.
use diary_management;
create view verifyLogin as
	select username, password from Users;
	
select * from verifyLogin;
--- drop view verifyLogin;

create table if not exists Users (
  User_ID int not null,
  username varchar(25) unique,
  password varchar(25),
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
SET FOREIGN_KEY_CHECKS = 0;
insert into users(user_id, username, password, has_admin, admin_id, creation_date, account_age) value
	(1, 'PixieNixie', '123456', 'yes', 7, '2024-03-20', 1),
	(2, 'HertBert', '98765', 'no', null, '2024-03-01', 1),
    (3, 'LeggoMyEggo', 'Sh00pDaW00p', 'yes', 7, '2020-03-08', 4);