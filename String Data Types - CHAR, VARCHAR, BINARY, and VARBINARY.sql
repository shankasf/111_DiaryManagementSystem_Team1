/*
Team 1
29 February 2024
CMPT 308N, Section 111
Phase 03: CHAR, VARCHAR, BINARY, and VARBINARY Examples
*/

/* MySQL is currently set on a mode that automatically trims CHAR values down to only the entered characters 
and excludes the padding. You can turn this off by using the following command:
SET SESSION sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';
*/
create database examples;
use examples;

drop database examples;

/* CHAR and VARCHAR */
create table trees (
	tree_name char(20) key,
    scientific_name varchar(25),
    endangered char
);

insert into trees (tree_name, scientific_name, endangered) values
	('White Oak', 'Quercus Alba', 'N'),
	('Giant Sequoia', 'Sequoiadendron Giganteum','Y'),
	('Red Maple', 'Acer Rubrum', 'N'),
	('Frasier Fir','Abies Fraseri','Y');

select * from trees;

/* select length(tree_name), length (scientific_name) from trees; */
drop table trees;

/* What happens if you exceed the default CHAR and VARCHAR values? */
insert into trees (tree_name, scientific_name, endangered) value
	('Grey Alder', 'Alnus Incana', 'No');
/* Answer: You get an error. The section "endangered" was set by default to the value 1. "No" is 
two characters, thus exceeding the specified value. */
/* This also occurs if the character count exceeds the maximum assigned to VARCHAR */
insert into trees (tree_name, scientific_name, endangered) value
	('Rayless Goldenhead', 'Acamptopappus Sphaerocephalus', 'N');


/* BINARY and VARBINARY */
create table stars (
	list_number binary,
    star_name varchar(30),
	radius_x_that_of_sun varbinary(4),
    distance_from_sun_in_light_years varbinary(6),
    speed_in_km_per_sec binary(6)
);

insert into stars (list_number, star_name, radius_x_that_of_sun, 
	distance_from_sun_in_light_years, speed_in_km_per_sec) values
	(1, 'Betelgeuse', 640, 500, 30),
	(2, 'Vega', 2.1, 25, 236),
	(3, 'Arcturus', 25, 36.7, 122),
	(4,'Spica', 7, 250, 199);

select * from stars;

/* select length(distance_from_sun_in_light_years), length (speed_in_km_per_sec) from stars; */
drop table stars;

/* And like CHAR and VARCHAR, you cannot insert a value that exceeds the set maximum value */
insert into stars (list_number, star_name, radius_x_that_of_sun, distance_from_sun_in_light_years, speed_in_km_per_sec) values
	(54, 'Sun', 0, 0, 251);