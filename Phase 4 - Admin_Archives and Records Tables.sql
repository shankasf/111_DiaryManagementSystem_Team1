/* 
Team 1
3/18/2024
CMPT 308N Section 111 (Database Management)
Phase 4: Admin_Archives and Records
*/

create database diary_management;
use diary_management;

/* drop database diary_management; */


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


create table records (
	record_id int primary key,
	record_name varchar(25),
    diary_id int,
    in_gallery enum('Yes', 'No'),
    gallery_id int,
    creation_date date,
    record_age date,
    record_description varchar(255)
);

insert into records (record_id, record_name, diary_id, in_gallery, gallery_id, creation_date, record_age, record_description) value
	(1, 'Test Record',  24, 'No', 42, '2024-03-01', '2024-03-18', 'A test of the records table');
select * from records;
/* drop table records; */