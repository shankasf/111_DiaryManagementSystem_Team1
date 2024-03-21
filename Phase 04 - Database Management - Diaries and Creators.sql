/* 
Team 1
3/20/2024
CMPT 308N Section 111 (Database Management)
Phase 4: Diaries and Creators
*/


create database diary_management;
use diary_management;

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

create table creators(
	creator_id int primary key,
    creator_type enum ('Creator', 'Admin')
);    

insert into creators (creator_id, creator_type) value
	(1, 'Admin');
select * from creators;
#drop table creators