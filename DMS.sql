create database if not exists Project_DMS;
use Project_DMS;

Create table if not exists Admins( 
	Admin_ID int,
	Name varchar (25) not null, 
	Creation_Date date not null,
	Account_Age date, 
	Archive_Num int,
	Primary Key(Admin_ID)
);

Create table if not exists Admin_Archives(
	Archive_Name varchar (25),
	Admin_ID int not null,
    Creator_Type enum('User', 'Group'),
    Creator_ID int not null,
    Record_ID int not null,
    Record_Description varchar(255),
    Primary Key (Archive_Name, Admin_ID),
		Foreign Key (Admin_ID) references Admins(Admin_ID)
		On Delete Cascade
);

Create table if not exists Users(
	User_ID int,
	Has_Admin enum('Yes','No'),
    Admin_ID int,
    Creation_Date date not null,
    Account_Age date,
    Primary Key (User_ID),
		Foreign Key (User_ID) references Creators(Creator_ID)
        On Delete Cascade
);	

Create table if not exists _Groups (
	Group_ID int,
	Creator_ID int,
    Creation_Date date not null,
    Group_Age date, 
    Member_Num int,
    Primary Key (Group_ID),
		Foreign Key (Group_ID) references Creators(Creator_ID)
        On Delete Cascade
);

Create table if not exists Creators (
	Creator_ID int,
    Creator_Type enum('User','Group'),
    Primary Key (Creator_ID)
);

Create table if not exists Diaries(
	Diary_ID int,
    Diary_Name varchar(25),
    Owner_Type enum('User','Group'),
    Owner_ID int not null,
    Creation_Date date,
    Diary_Age date,
    Record_Num int,
    Gallery_Num int,
	Primary Key (Owner_ID, Owner_Type, Diary_ID),
		Foreign Key (Owner_ID, Owner_Type) references Creators(Creator_ID, Creator_Type)
		On Delete Cascade
);

Create table if not exists Records(
	Record_ID int,
    Diary_ID int,
    In_Gallery enum ('Yes', 'No'),
    Galley_ID int,
    Creation_Date date,
    Record_Age date,
    Record_Name varchar(25),
    Record_Description varchar (255),
    Primary Key (Record_ID, Diary_ID),
		Foreign Key (Diary_ID) references Diaries(Diary_ID)
);

Create table if not exists Galleries(
	Gallery_ID int,
    Diary_ID int,
    Creation_Date date,
    Gallery_Name varchar (25),
    Gallery_Age date,
    Record_Num int,
    Primary Key(Galley_ID, Diary_ID),
		Foreign Key (Diary_ID) references Diaries(Diary_ID)
);

Create table if not exists Planners(
	Planner_ID int,
    Planner_Name varchar(25),
    Owner_Type enum('User','Group'),
    Owner_ID int not null,
    Creation_Date date,
    Planner_Age date,
    Task_Num int,
    Checklist_Num int,
	Primary Key (Owner_ID, Owner_Type, Planner_ID),
		Foreign Key (Owner_ID, Owner_Type) references Creators(Creator_ID, Creator_Type)
		On Delete Cascade
);

Create table if not exists Tasks(
	Task_ID int,
    Planner_ID int,
    In_Checklist enum ('Yes', 'No'),
    Checklist_ID int,
    Creation_Date int,
    Task_Due_Date date,
    Task_Name varchar(25),
    Task_Description varchar (255),
    Primary Key (Task_ID, Planner_ID),
		Foreign Key (Planner_ID) references Planners(Planner_ID)
);

Create table if not exists Checklists(
	Checklist_ID int,
    Planner_ID int,
    Creation_Date date,
    Checklist_Name varchar (25),
    Checklist_Age date,
    Task_Num int,
    Primary Key(Checklist_ID, Planner_ID),
		Foreign Key (Planner_ID) references Planners(Planner_ID)
);