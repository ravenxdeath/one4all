show databases;
create database lab01_db;
use lab01_db;

create table LabGrades (
	stdID char(4),
    name varchar(30),
    major char(3),
    section char(1),
    daysPresent int,
    projectMarks double,
    cgpa decimal (3,2),
    submissionDate date
    );

show tables;
describe labgrades;

INSERT INTO LabGrades values
('s001', 'Abir', 'CS', '1', 10, 18.5, 3.91, '2018-09-15' ),
('s002', 'Nafis', 'CSE', '1', 12, 20, 3.86, '2018-08-15' ),
('s003', 'Tasneem', 'CS', '1', 8, 18, 3.57, '2018-09-18' ),
('s004', 'Nahid', 'ECE', '2', 7, 16.5, 3.25, '2018-08-20' ),
('s005', 'Arafat', 'CS', '2', 11, 20, 4, '2018-09-13' ),
('s006', 'Tasneem', 'CSE', '1', 12, 17.5, 3.7, '2018-08-15' ),
('s007', 'Muhtadi', 'ECE', '1', 10, 19, 3.67, '2018-09-16' ),
('S008', 'Farhana', 'CSE', '2', 6, 15, 2.67, '2018-08-16' ),
('s009', 'Naima', 'CSE', '2', 12, 20, 3.7, '2018-08-14' );

describe labGrades;
show tables;
select *from labGrades;

alter table labGrades add ProjectTitle 	char(10);
alter table labGrades modify column ProjectTitle varchar(50);
alter table labGrades drop column ProjectTitle;

alter table labGrades rename column submissionDate to subDate; 
-- alter table column name
/* multi line comment 
*/

set sql_safe_updates = 0;
Update LabGrades set major="CSE" where name= "Arafat";
Update LabGrades set name= "Naheed", projectMarks= 16 where stdID="s004";
set sql_safe_updates = 1;

Select name, projectMarks+daysPresent/12*5 as TotalMarks from LabGrades;

Select major from LabGrades;
Select distinct major from LabGrades;
Select *from LabGrades order by name;
Select *from LabGrades order by name desc, submissionDate asc;

Select name, projectMarks from LabGrades where projectMarks between 17 and 19;
Select name, projectMarks from LabGrades where projectMarks in(17,19);

Select *from LabGrades where name like "a%";
Select *from LabGrades where name like "%a%a%";



