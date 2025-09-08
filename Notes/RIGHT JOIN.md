
# RIGHT JOIN

[[🏷️SQL]]

When joining two tables, `RIGHT JOIN` returns all of the records of the second table, but only returns rows from the first table that match on a specified column.

![[Image 2.84.png]]

The following query demonstrates the syntax for `RIGHT JOIN`:

```sql 
SELECT *
FROM employees
RIGHT JOIN machines 
ON employees.device_id = machines.device_id;
```

`RIGHT JOIN` has the same syntax as `LEFT JOIN`, with the only difference being the keyword `RIGHT JOIN` instructs SQL to produce different output. The query returns all records from `machines`, which is the second or right table. Only matching records are returned from `employees`, which is the first or left table.

> [!note]
> You can use `LEFT JOIN` and `RIGHT JOIN` and return the exact same results if you use the tables in reverse order. The following `RIGHT JOIN` query returns the exact same result as the `LEFT JOIN` query demonstrated in the previous section:

```sql
SELECT *
FROM machines
RIGHT JOIN employees 
ON employees.device_id = machines.device_id;
```

All that you have to do is switch the order of the tables that appear before and after the keyword used for the join, and you will have swapped the left and right table.
