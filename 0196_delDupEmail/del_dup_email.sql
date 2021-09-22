delete from Person where Id in
(select Id from (select min(Id) Id, Email from Person group by Email) b);
