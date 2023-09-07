SELECT machine_id, ROUND((finish - init) / processes, 3) AS processing_time
  FROM (SELECT machine_id,
               COUNT(*) / 2 AS processes,
               SUM(IF(activity_type = 'start', timestamp, 0)) AS init,
               SUM(IF(activity_type = 'end',   timestamp, 0)) AS finish
          FROM Activity
         GROUP BY machine_id) s
