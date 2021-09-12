select a.name as employee from employee a
left join employee b
    on a.managerId = b.id
where a.salary > b.salary;0