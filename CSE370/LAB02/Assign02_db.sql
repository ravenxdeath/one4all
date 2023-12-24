create database Assign02_db;
show databases;
use Assign02_db;

show tables;

create table employees (
    employee_id char(10),
    first_name varchar(20),
    last_name varchar(20),
    email varchar(60),
    phone_number char(14),
    hire_date date,
    job_id char(10),
    salary int,
    commission_pct decimal(5,3),
    manager_id char(10),
    department_id char(10)
);
select *from employees;

insert into employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
values
    ('EMP001', 'Monkey D.', 'Luffy', 'luffy@gmail.com', '01712345678', '2023-10-19', 'JOB001', 80000, 0.050, 'MNG001', 'DPT001'),
    ('EMP002', 'Roronoa', 'Zoro', 'zoro@yahoo.com', '01723456789', '2023-10-20', 'JOB002', 70000, 0.040, 'MNG001', 'DPT001'),
    ('EMP003', 'Nami', 'Cat Burglar', 'nami@protonmail.com', '01734567890', '2023-10-21', 'JOB003', 30000, 0.060, 'MNG002', 'DPT002'),
    ('EMP004', 'Usopp', 'Sniper King', 'usopp@gmail.com', '01745678901', '2023-10-22', 'JOB004', 25000, 0.035, 'MNG002', 'DPT002'),
    ('EMP005', 'Sanji', 'Vinsmoke', 'sanji@yahoo.com', '01756789012', '2023-10-23', 'JOB005',65000, 0.055, 'MNG003', 'DPT003'),
    ('EMP006', 'Tony Tony', 'Chopper', 'tony@gmail.com', '01767890123', '2023-10-24', 'JOB006', 20000, 0.045, 'MNG002', 'DPT004'),
    ('EMP007', 'Nico', 'Robin', 'nico@protonmail.com', '01778901234', '2023-10-25', 'JOB007', 68000, 0.070, 'MNG003', 'DPT005'),
    ('EMP008', 'Franky', 'Cutty Flam', 'franky@gmail.com', '01789012345', '2023-10-26', 'JOB008', 51000, 0.050, 'MNG003', 'DPT006'),
    ('EMP009', 'Brook', 'Soul King', 'brook@yahoo.com', '01790123456', '2023-10-27', 'JOB009', 49000, 0.045, 'MNG003', 'DPT007'),
    ('EMP010', 'Jinbe', 'Knight of the Sea', 'jinbe@gmail.com', '01701234567', '2023-10-28', 'JOB010', 54000, 0.065, 'MNG004', 'DPT007');
    
select first_name, last_name, email, phone_number, hire_date, department_id
from employees
where hire_date = (select max(hire_date) from employees);

select e1.first_name, e1.last_name, e1.employee_id, e1.phone_number, e1.salary, e1.department_id
from employees e1
where (e1.department_id, e1.salary) in (
    select e2.department_id, min(e2.salary)
    from employees e2
    group by e2.department_id
);

select e1.first_name, e1.last_name, e1.employee_id, e1.commission_pct, e1.department_id
from employees e1
where e1.department_id = 'dpt007'
and e1.commission_pct < all (
    select e2.commission_pct
    from employees e2
    where e2.department_id = 'dpt005'
);

select department_id, count(*) as total_employees
from employees
group by department_id
having max(salary) <= 30000;

select e1.department_id, e1.job_id, e1.commission_pct
from employees e1
where e1.commission_pct < any (
    select e2.commission_pct
    from employees e2
    where e2.department_id = e1.department_id
    and e2.job_id <> e1.job_id
);
select manager_id
from employees
group by manager_id
having min(salary) >= 3500;

select e1.first_name, e1.last_name, e1.employee_id, e1.email, e1.salary, e1.department_id, e1.commission_pct
from employees e1
where (e1.manager_id is not null) and (
    e1.commission_pct = (select min(commission_pct) from employees e2 where e2.manager_id = e1.manager_id)
);


