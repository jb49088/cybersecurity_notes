
# FULL OUTER JOIN

[[🏷️SQL]]

`FULL OUTER JOIN` returns all records from both tables. You can think of it as a way of completely merging two tables.

![[Image 2.85.png]]

You can review the syntax for using `FULL OUTER JOIN` in the following query:

```sql
SELECT *
FROM employees
FULL OUTER JOIN machines 
ON employees.device_id = machines.device_id;
```

The results of a `FULL OUTER JOIN` query include all records from both tables. Similar to `INNER JOIN`, the order of tables does not change the results of the query.