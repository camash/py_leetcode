delete from Person where Id not in
(select Id from (select min(Id) Id, Email from Person group by Email) b);
