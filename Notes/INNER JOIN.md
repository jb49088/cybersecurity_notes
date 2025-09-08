
# INNER JOIN

[[🏷️SQL]]

The first type of join that you might perform is an inner join. `INNER JOIN` returns rows matching on a specified column that exists in more than one table.

![[Image 2.82.png]]

It only returns the rows where there is a match, but like other types of joins, it returns all specified columns from all joined tables. For example, if the query joins two tables with `SELECT *`, all columns in both of the tables are returned.

> [!note]
> If a column exists in both of the tables, it is returned twice when `SELECT *` is used.

## The syntax of an inner join

To write a query using `INNER JOIN`, you can use the following syntax:

```sql
SELECT *
FROM employees
INNER JOIN machines 
ON employees.device_id = machines.device_id;
```

You must specify the two tables to join by including the first or left table after `FROM` and the second or right table after `INNER JOIN`.

After the name of the right table, use the `ON` keyword and the `=` operator to indicate the column you are joining the tables on. It's important that you specify both the table and column names in this portion of the join by placing a period (`.`) between the table and the column.

In addition to selecting all columns, you can select only certain columns.  For example, if you only want the join to return the `username`, `operating_system` and `device_id` columns, you can write this query:

```sql
SELECT username, operating_system, employees.device_id
FROM  employees
INNER JOIN machines 
ON employees.device_id = machines.device_id;
```

> [!note]
> In the example query, `username` and `operating_system` only appear in one of the two tables, so they are written with just the column name. On the other hand, because `device_id` appears in both tables, it's necessary to indicate which one to return by specifying both the table and column name (`employees.device_id`).


