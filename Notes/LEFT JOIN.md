
# LEFT JOIN

[[🏷️SQL]]

When joining two tables, `LEFT JOIN` returns all the records of the first table, but only returns rows of the second table that match on a specified column.

![[Image 2.83.png]]

## The syntax of a left outer join

```sql
SELECT *
FROM employees
LEFT JOIN machines 
ON employees.device_id = machines.device_id;
```

As with all joins, you should specify the first or left table as the table that comes after `FROM` and the second or right table as the table that comes after `LEFT JOIN`. In the example query, because `employees` is the left table, all of its records are returned. Only records that match on the `device_id` column are returned from the right table, `machines`.
