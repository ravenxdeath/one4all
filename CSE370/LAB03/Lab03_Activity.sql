show databases;
create database lab03_db;
show databases;
use lab03_db;

create table customer (
customer_id varchar(10) not null,
customer_name varchar(20) not null,
customer_street varchar(30),
customer_city varchar(30),
primary key (customer_id)
);
show tables;
select *from branch;

create table branch (
branch_name varchar(15),
branch_city varchar(30),
assets int,
primary key (branch_name),
check (assets >= 0)
);

create table account (
branch_name varchar(15),
account_number varchar(10) not null,
balance int,
primary key (account_number),
check (balance >= 0)
);

create table loan (
loan_number varchar(10) not null,
branch_name varchar(15),
amount int,
primary key (loan_number)
);

create table depositor (
customer_id varchar(10) not null,
account_number varchar(10) not null,
primary key (customer_id, account_number),
foreign key (customer_id) references customer(customer_id),
foreign key (account_number) references account(account_number)
);

create table borrower (
customer_id varchar(10) not null,
loan_number varchar(10) not null,
primary key (customer_id, loan_number),
foreign key (customer_id) references customer(customer_id),
foreign key (loan_number) references loan(loan_number)
);

show tables;

insert into customer values
('c-101','Jones', 'Main', 'Harrison'),
('c-201','Smith', 'North', 'Rye'),
('c-211','Hayes', 'Main', 'Harrison'),
('c-212','Curry', 'North', 'Rye'),
('c-215','Lindsay', 'Park', 'Pittsfield'),
('c-220','Turner', 'Putnam', 'Stamford'),
('c-222','Williams', 'Nassau', 'Princeton'),
('c-225','Adams', 'Spring', 'Pittsfield'),
('c-226','Johnson', 'Alma', 'Palo Alto'),
('c-233','Glenn', 'Sand Hill', 'Woodside'),
('c-234','Brooks', 'Senator', 'Brooklyn'),
('c-255','Green', 'Walnut', 'Stamford');

insert into branch values
('downtown', 'brooklyn',9000000),
('redwood', 'palo alto',2100000),
('perryridge', 'horseneck',1700000),
('mianus', 'horseneck',400000),
('round hill', 'horseneck',8000000),
('pownal', 'bennington',300000),
('north town', 'rye',3700000),
('brighton', 'brooklyn',7100000);

insert into account
values
('downtown','a-101',500),
('mianus','a-215',700),
('perryridge','a-102',400),
('round hill','a-305',350),
('brighton','a-201',900),
('redwood','a-222',700),
('brighton','a-217',750);

insert into loan
values
('l-17', 'downtown', 1000),
('l-23', 'redwood', 2000),
('l-15', 'perryridge', 1500),
('l-14', 'downtown', 1500),
('l-93', 'mianus', 500),
('l-11', 'round hill', 900),
('l-16', 'perryridge', 1300);

insert into depositor
values
('c-226', 'a-101'),
('c-201', 'a-215'),
('c-211', 'a-102'),
('c-220', 'a-305'),
('c-226', 'a-201'),
('c-101', 'a-217'),
('c-215', 'a-222');

insert into borrower
values
('c-101', 'l-17'),
('c-201', 'l-23'),
('c-211', 'l-15'),
('c-226', 'l-14'),
('c-212', 'l-93'),
('c-201', 'l-11'),
('c-222', 'l-17'),
('c-225', 'l-16');

select *from customer;
-- inner join common data joins
select c.customer_id, c.customer_name, c.customer_city, a.account_number
from customer c
inner join depositor d on c.customer_id = d.customer_id
inner join account a on d.account_number = a.account_number;

-- left join
select c.customer_id, c.customer_name, c.customer_city, a.account_number
from customer c
left join depositor d on c.customer_id = d.customer_id
left join account a on d.account_number = a.account_number;

-- right join
select c.customer_id, c.customer_name, c.customer_city, a.account_number
from customer c
right join depositor d on c.customer_id = d.customer_id
right join account a on d.account_number = a.account_number;

select c.customer_name, c.customer_city, a.account_number, a.balance, b.branch_name
from customer c
join depositor d on c.customer_id = d.customer_id
join account a on d.account_number = a.account_number
join branch b on a.branch_name = b.branch_name;

-- same without using join
SELECT c.customer_name, c.customer_city, a.account_number, a.balance, b.branch_name
FROM customer c, depositor d, account a, branch b
WHERE c.customer_id = d.customer_id
  AND d.account_number = a.account_number
  AND a.branch_name = b.branch_name;

-- Find names and cities of customers who have a loan at Perryridge branch.
select c.customer_name, c.customer_city
from customer c, borrower b, loan l, branch br
where c.customer_id = b.customer_id
  and b.loan_number = l.loan_number
  and l.branch_name = br.branch_name
  and br.branch_name = 'perryridge';
  
-- Find which accounts with balances between 700 and 900:
select account_number, balance
from account
where balance >= 700 and balance <= 900;

-- Find the names of customers on streets with names ending in "hill":
select customer_name
from customer
where customer_street like '%hill';

-- Find the names of branches whose assets are greater than the assets of some branch in Brooklyn:
select distinct b1.branch_name
from branch b1, branch b2
where b1.assets > (select assets from branch where branch_city = 'brooklyn' and branch_name = b2.branch_name);

-- Find the set of names of branches whose assets are greater than the assets of all branches in Horseneck:
select branch_name
from branch
where assets > all (select assets from branch where branch_city = 'horseneck');

-- Find the set of names of customers at Brighton branch, in alphabetical order:

select customer_name
from customer c, depositor d, account a, branch b
where c.customer_id = d.customer_id
  and d.account_number = a.account_number
  and a.branch_name = b.branch_name
  and b.branch_name = 'brighton'
order by customer_name;

-- Show the loan data, ordered by decreasing amounts, then increasing loan numbers:

select *
from loan
order by amount desc, loan_number;

-- Find the names of branches having at least one account, with average balances greater than or equal 700:

select b.branch_name
from branch b, account a
where b.branch_name = a.branch_name
group by b.branch_name
having avg(a.balance) >= 700;

-- Find the names and account numbers of customers who have the 3 highest balances in their accounts:
select c.customer_name, a.account_number
from customer c, account a
where c.customer_id = a.branch_name
order by a.balance desc
limit 3;









