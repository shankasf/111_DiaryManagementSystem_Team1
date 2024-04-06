create database StringDataTypes;
use StringDataTypes;
drop table StringDataTypeEx;
create table StringDataTypeEx (
blobDescription BLOB,
textDescription TINYTEXT,
level ENUM('L_one', 'L_two', 'L_three'),
col SET('a', 'b', 'c')
);

insert into StringDataTypeEx(blobDescription, textDescription, level, col)
 values ('Blob description', 'text','L_one', 'a');
 
 select * from StringDataTypeEx;
