WITH started AS (SELECT player_id, MIN(event_date) AS event_date
                   FROM Activity
                  GROUP BY player_id)
SELECT ROUND((SELECT COUNT(DISTINCT a.player_id) AS player_id
                FROM started s, Activity a
               WHERE s.player_id = a.player_id
                 AND s.event_date = DATE_SUB(a.event_date, INTERVAL 1 DAY)) /
             (SELECT COUNT(DISTINCT player_id)
                FROM Activity), 2) AS fraction
