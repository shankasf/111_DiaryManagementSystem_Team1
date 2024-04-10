/* 
Team 1
4/3/2024
CMPT 308N Section 111 (Database Management)
Phase 6
*/
create database if not exists diary_management;
use diary_management;

create view verifyLogin as
select Username, Password from Users;
select * from verifyLogin;
--- drop view verifyLogin;

create view Admin_Adminee_Requests as
select Admin_ID, Creator_ID where Adminee_Status = 'Requested';
select * from Admin_Adminee_Requests;
-- drop view Admin_Adminee_Requests;

create view Admin_Adminee_Established as
select Admin_ID, Creator_ID where Adminee_Status = 'Established';
select * from Admin_Adminee_Established;
-- drop view Admin_Adminee_Established;

create view Admin_Archived_Record as 
select Admin_ID, Creator_ID, Record_ID from Admin_Archives;
select * from Admin_Archived_Record;
-- drop view Admin_Archved_Record;

create view Admin_Search as
select Admin_ID, User_ID from Admin_Users;
select * from Admin_Search;
-- drop view Admin_Search;

create view NonArchived_Records as
select Admin_ID, Creator_ID, Record_ID from Admin_Archives;
select * from NonArchived_Records;
-- drop view NonArchived_Records;

create view Group_Search as
select Group_ID, User_ID from _Groups full join Users;
select * from Group_Search;
-- drop view Group_Search;

create view Diary_Info as 
select Diaries.Diary_ID, Creator_ID, Record_ID, Galleries.Gallery_ID
from Diaries
join Galleries on Diaries.Diary.ID = Galleries.Diary_ID
join Records on Diaries.Diary_ID = Records.Diary_ID
join Creators on Creators.Creator_ID = Creator_ID;
select * from Diary_Info;
-- drop view Diary_Info;

create view Planner_Info as
select c.Creator_ID, p.Planner_ID, p.Owner_ID, t.Task_ID, cl.Checklist_ID
from Creators c
join Planners p on p.Owner_ID = c.Creator_ID
join Tasks t on t.Planner_ID = p.Planner_ID
join Checklists cl on cl.Planner_ID = p.Planner_ID;
select * from Planner_Info;
-- drop view Planner_Info;
