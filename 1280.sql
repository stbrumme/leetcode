WITH crossed AS (SELECT st.student_id, st.student_name, su.subject_name
                   FROM Students st, Subjects su) -- all combinations
SELECT c.student_id, c.student_name, c.subject_name,
       COUNT(e.subject_name) AS attended_exams
  FROM crossed c LEFT JOIN Examinations e
    ON c.student_id = e.student_id AND c.subject_name = e.subject_name
 GROUP BY c.student_id, c.subject_name
 ORDER BY c.student_id, c.subject_name
