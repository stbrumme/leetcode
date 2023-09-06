SELECT worker.name AS Employee
  FROM Employee worker, Employee manager
 WHERE worker.managerId = manager.id
   AND worker.salary > manager.salary
