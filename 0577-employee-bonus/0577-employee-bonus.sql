# Write your MySQL query statement below
select a.name , p.bonus 
from employee a
left join bonus p
on a.empId = p.empId
where bonus < 1000 OR 
p.bonus is null