show databases;

create database labAss01db;
use labAss01db;

create table Developers (
	member_id int,
	name varchar (50),
	email varchar(100),
	influence_count int,
	Joining_date date,
	multiplier int
);

show tables;
describe developers;
select *from developers;

insert into developers 
values
    (1, 'Taylor Otwell', 'otwell@laravel.com', 739360, '2020-06-10', 10),
    (2, 'Ryan Dahl', 'ryan@nodejs.org', 633632, '2020-04-22', 10),
    (3, 'Brendan Eich', 'eich@javascript.com', 939570, '2020-05-07', 8),
    (5, 'Evan You', 'you@vuejs.org', 982630, '2020-06-11', 7),
    (6, 'Rasmus Lerdorf', 'lerdorf@php.net', 937927, '2020-06-03', 8),
    (7, 'Guido van Rossum', 'guido@python.org', 968827, '2020-07-18', 19),
    (8, 'Adrian Holovaty', 'adrian@djangoproject.com', 570724, '2020-05-07', 5),
    (9, 'Simon Willison', 'simon@djangoproject.com', 864615, '2020-04-30', 4),
    (10, 'James Gosling', 'james@java.com', 719491, '2020-05-18', 5),
    (11, 'Rod Johnson', 'rod@spring.io', 601744, '2020-05-18', 7),
    (12, 'Satoshi Nakamoto', 'nakamoto@blockchain.com', 630488, '2020-05-10', 10);
    
/*DELETE FROM Developers
ORDER BY member_id DESC
LIMIT 12;
*/

select *from developers;
alter table developers rename column influence_count to followers;
alter table developers modify column followers int;
describe developers;

update developers set followers = followers +10;
select *from developers;

alter table developers add efficiency decimal(10,3);
ALTER table Developers
drop column Efficiency;

select name, cast(((followers * 100.0 / 1000000) * (multiplier * 100.0 / 20)) / 100 as decimal(5, 2)) as Efficiency
from Developers;

/* used cast to explicitly get the desired data type e.g. here decimal(5,2) */


select upper(name) as JoinedLast from developers order by joining_date desc;


select member_id,name,email,followers from Developers
where email like '%.com' or email like '%.net';