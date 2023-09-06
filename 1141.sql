WITH uniq AS (SELECT activity_date, user_id
                FROM Activity
               GROUP BY activity_date, user_id)
SELECT activity_date AS `day`, COUNT(*) AS active_users
  FROM uniq
 WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
 GROUP BY activity_date
