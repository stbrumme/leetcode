DELETE FROM Person
 WHERE id NOT IN (SELECT MIN(id)
                    FROM (SELECT * FROM Person) p -- MySQL needs to have a temporary copy
                   GROUP BY email)
