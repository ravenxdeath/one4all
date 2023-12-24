show databases;
create database bank;
use bank;

create table customer (
    customer_id varchar(10) not null,
    customer_name varchar(20) not null,
    customer_street varchar(30),
    customer_city varchar(30),
    primary key (customer_id)
);

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

SHOW TABLES;

insert into customer values
('C-101', 'Jones', 'Main', 'Harrison'),
('C-201', 'Smith', 'North', 'Rye'),
('C-211', 'Hayes', 'Main', 'Harrison'),
('C-212', 'Curry', 'North', 'Rye'),
('C-215', 'Lindsay', 'Park', 'Pittsfield'),
('C-220', 'Turner', 'Putnam', 'Stamford'),
('C-222', 'Williams', 'Nassau', 'Princeton'),
('C-225', 'Adams', 'Spring', 'Pittsfield'),
('C-226', 'Johnson', 'Alma', 'Palo Alto'),
('C-233', 'Glenn', 'Sand Hill', 'Woodside'),
('C-234', 'Brooks', 'Senator', 'Brooklyn'),
('C-255', 'Green', 'Walnut', 'Stamford');

insert into branch values
('Downtown', 'Brooklyn', 9000000),
('Redwood', 'Palo Alto', 2100000),
('Perryridge', 'Horseneck', 1700000),
('Mianus', 'Horseneck', 400000),
('Round Hill', 'Horseneck', 8000000),
('Pownal', 'Bennington', 300000),
('North Town', 'Rye', 3700000),
('Brighton', 'Brooklyn', 7100000);

insert into account values
('Downtown', 'A-101', 500),
('Mianus', 'A-215', 700),
('Perryridge', 'A-102', 400),
('Round Hill', 'A-305', 350),
('Brighton', 'A-201', 900),
('Redwood', 'A-222', 700),
('Brighton', 'A-217', 750);

insert into loan values
('L-17', 'Downtown', 1000),
('L-23', 'Redwood', 2000),
('L-15', 'Perryridge', 1500),
('L-14', 'Downtown', 1500),
('L-93', 'Mianus', 500),
('L-11', 'Round Hill', 900),
('L-16', 'Perryridge', 1300);

insert into depositor values
('C-226', 'A-101'),
('C-201', 'A-215'),
('C-211', 'A-102'),
('C-220', 'A-305'),
('C-226', 'A-201'),
('C-101', 'A-217'),
('C-215', 'A-222');

insert into borrower values
('C-101', 'L-17'),
('C-201', 'L-23'),
('C-211', 'L-15'),
('C-226', 'L-14'),
('C-212', 'L-93'),
('C-201', 'L-11'),
('C-222', 'L-17'),
('C-225', 'L-16');

select * from customer;
select * from branch;
select * from account;
select * from loan;
select * from depositor;
select * from borrower;

-- 1. Find the name and loan number of all customers having a loan at the Downtown branch.

select c.customer_name, l.loan_number
from customer c, borrower b, loan l, branch br
where c.customer_id = b.customer_id
and b.loan_number = l.loan_number
and l.branch_name = br.branch_name
and br.branch_name = 'Downtown';

-- or
select c.customer_name, l.loan_number
from customer c
join borrower b on c.customer_id = b.customer_id
join loan l on b.loan_number = l.loan_number
join branch br on l.branch_name = br.branch_name
where br.branch_name = 'Downtown';

/* 2. Find all the possible pairs of customers who are from the same city.
     show in the format Customer1, Customer2, City. */

select distinct c1.customer_name as customer1, c2.customer_name as customer2, c1.customer_city as city
from customer c1, customer c2
where c1.customer_city = c2.customer_city
and c1.customer_id < c2.customer_id;

-- or
select distinct c1.customer_name as customer1, c2.customer_name as customer2, c1.customer_city as city
from customer c1
join customer c2 on c1.customer_city = c2.customer_city and c1.customer_id < c2.customer_id;

/*3. If the bank gives out 4% interest to all accounts, show the total interest across each
branch. Print Branch_name, Total_Interest */
select a.branch_name, sum(a.balance * 0.04) as total_interest
from account a
group by a.branch_name;

/*  Find account numbers with the highest balances for each city in the database */

select a.branch_name, a.account_number, a.balance
from account a
where (a.branch_name, a.balance) in (
    select branch_name, max(balance)
    from account
    group by branch_name
);

select a1.branch_name, a1.account_number, a1.balance
from account a1
where a1.balance = (select max(a2.balance) from account a2 where a2.branch_name = a1.branch_name);

SELECT branch_name AS city, MAX(balance) AS highest_balance
FROM account
GROUP BY branch_name;





/*Show the loan number, loan amount, and name of customers who have the top 5
highest loan amounts. The data should be sorted by increasing amounts, then
decreasing loan numbers in case of the same loan amount. [Hint for top 5 check the
"limit" keyword in mysql] */
select l.loan_number, l.amount, c.customer_name
from loan l
join borrower b on l.loan_number = b.loan_number
join customer c on b.customer_id = c.customer_id
order by l.amount asc, l.loan_number desc
limit 5;

-- Find the names of customers with an account and also a loan at the Perryridge branch.

select distinct c.customer_name
from customer c
inner join depositor d on c.customer_id = d.customer_id
inner join account a on d.account_number = a.account_number
inner join borrower b on c.customer_id = b.customer_id
inner join loan l on b.loan_number = l.loan_number
where a.branch_name = 'Perryridge' and l.branch_name = 'Perryridge';

-- or
select distinct c.customer_name
from customer c
where c.customer_id in (
    select distinct d.customer_id
    from depositor d
    where d.account_number in (
        select distinct a.account_number
        from account a
        where a.branch_name = 'Perryridge'
    )
) and c.customer_id in (
    select distinct b.customer_id
    from borrower b
    where b.loan_number in (
        select distinct l.loan_number
        from loan l
        where l.branch_name = 'Perryridge'
    )
);

/*  Find the total loan amount of all customers having at least 2 loans from the bank. 
Show in format customer name, total_loan. */

select c.customer_name, sum(l.amount) as total_loan
from customer c
join borrower b on c.customer_id = b.customer_id
join loan l on b.loan_number = l.loan_number
group by c.customer_name
having count(l.loan_number) >= 2;
