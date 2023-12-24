show databases;
create database lab02_db;
use lab02_db;

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

set sql_safe_updates = 0;
Update LabGrades set major="CSE" where name= "Arafat";
Update LabGrades set name= "Naheed", projectMarks= 16 where stdID="s004";
set sql_safe_updates = 1;

DELETE FROM labgrades
WHERE stdID IN ('s004', 's008', 's009');

select min(CGPA) from labgrades;
select count(*) as totalStudents, avg(projectMarks) as avgProjectMarks from labGrades;
select sum(daysPresent) from labgrades;

select major,min(CGPA) as minCGPA, max(CGPA) as maxCGPA from labGrades group by major;
select major,count(*) from labGrades group by major;

select major,min(CGPA) as minCGPA, max(CGPA) as maxCGPA from labGrades group by major having count(*)>=2;
select major,min(CGPA) as minCGPA, max(CGPA) as maxCGPA from labGrades
where subDate<="2018-09-15" group by major;

select *from labGrades;

select name from labGrades where projectMarks= (select max(projectMarks) from labGrades); 
select major, name, daysPresent from labgrades where(major, daysPresent) in (select major, min(daysPresent) from labgrades group by major);

select *from labGrades where major=	"CSE" and CGPA > any 
(select CGPA from labGrades where major = "CS");

select *from labGrades where major=	"CSE" and CGPA > all 
(select CGPA from labGrades where major = "CS");

-- correlation is updown Aprroach we take outer querry and then into inner query 

select distinct major from labGrades L1 where exists (select *from labGrades L2 where L2.major= L1.major and L2.major <3.7);
